class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = ceil(sum(piles) / h)
        right = max(piles)
        answer = right

        while left <= right:
            target = (left + right) // 2
            hours = 0

            for pile in piles:            
                hours += ceil(pile / target)
            
            if hours <= h:
                answer = target
                right = target - 1
            else:
                left = target + 1
        
        return answer
