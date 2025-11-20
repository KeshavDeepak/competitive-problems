class Solution:
    def findTwoElement(self, arr):
        # code here
        all = set(i for i in range(1, len(arr) + 1))
        answer = [-1, -1]
        
        for num in arr:
            if num not in all: # is the repeating number
                answer[0] = num
            else:
                all.remove(num) # remove num 
        
        answer[1] = list(all)[0]
        
        return answer


# more efficient solution using sum and squared sum
'''
class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        s_full = (n * (n + 1)) // 2
        s2_full = (n * (n+1) * (2*n+1)) // 6
        
        s = 0
        s2 = 0
        
        for num in arr:
            s += num
            s2 += num ** 2
        
        # x = repeating element
        # y = missing element
        
        # s_full + x - y = s
        # s2_full + x**2 - y**2 = s2
        
        # y - x
        sub = s_full - s
        
        # y**2 - x**2
        sub2 = s2_full - s2
        
        # y + x
        add = sub2 // sub
        
        x = (sub - add) // -2
        y = add - x
        
        return [x, y]
'''