class Solution:
    def canCross(self, stones: list[int]) -> bool:
        hash = {}

        for idx, stone in enumerate(stones):
            hash[stone] = idx
        
        self.dp = {}

        def f(i, k):
            # base cases
            if i == len(stones)-1: # last stone has been reached
                return True 
            
            if (i, k) in self.dp: # cache
                return self.dp[(i, k)]

            # recursive case
            answer = False

            # -- is stones[i]+k-1 > 0 and a stone
            if (k-1) > 0 and (stones[i]+k-1) in hash:
                answer = answer or f(hash[stones[i]+k-1], k-1)
            
            # -- is stones[i]+k+1 a stone
            if (stones[i]+k+1) in hash:
                answer = answer or f(hash[stones[i]+k+1], k+1)
            
            # -- is stones[i]+k a stone?
            if (stones[i]+k) in hash:
                answer = answer or f(hash[stones[i]+k], k)
            
            # memoize
            self.dp[(i, k)] = answer

            #
            return answer
        
        # ensure it is possible to jump to second stone
        if stones[1] - stones[0] > 1:
            return False
        
        #
        return f(1, 1)