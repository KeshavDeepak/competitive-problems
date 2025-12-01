class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left = 1
        right = sum(batteries) // n
        answer = left

        while left <= right:
            mid = (left + right) // 2
            total = 0

            for battery in batteries:
                total += min(battery, mid)
            
            if total >= mid * n:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return answer
