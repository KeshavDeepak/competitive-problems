from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([beginWord])
        answer = 1
        wordList_set = set(wordList)

        # edge case
        if endWord not in wordList_set:
            return 0

        # bfs from beginWord and see if we can reach endWord
        while queue:
            curr_len = len(queue)

            for _ in range(curr_len):
                curr_word = queue.popleft()

                for index in range(len(curr_word)):
                    for letter in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = curr_word[:index] + letter + curr_word[index+1:]

                        if new_word in wordList_set:
                            if new_word == endWord: # found endWord
                                return answer + 1
                            else: # add to queue
                                queue.append(new_word)
                                wordList_set.remove(new_word)
                
            answer += 1
        
        # if no endWord found, default to 0
        return 0


