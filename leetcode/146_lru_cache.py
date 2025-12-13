class Node:
    def __init__(self, val=0, key=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
    
    def makeHighest(self, node):
        # update priority of key
        # -- remove node from linked list
        node.prev.next = node.next
        node.next.prev = node.prev

        # -- place node after head
        node.next = self.head.next
        node.next.prev = node

        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # retrieve node
            node = self.hashmap[key]

            # make highest priority
            self.makeHighest(node)

            # 
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if key already exists, simply update, prioritize and return
        if key in self.hashmap:
            node = self.hashmap[key]

            # make highest priority
            self.makeHighest(node)

            # update value
            node.val = value

            #
            return
        
        # add new node
        # -- if no space, remove lru node
        if len(self.hashmap) == self.capacity:
            del_key = self.tail.prev.key
            new_last = self.tail.prev.prev

            new_last.next = self.tail
            self.tail.prev = new_last

            del self.hashmap[del_key]
        
        # -- add new node as highest priority
        new = Node(value, key)

        # -- -- add in front of head
        new.next = self.head.next
        new.next.prev = new

        self.head.next = new
        new.prev = self.head

        # -- update hashmap
        self.hashmap[key] = new

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
