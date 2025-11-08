class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        # base case
        if len(colors) == 1: return 0

        # pointers
        left = 0
        right = 1

        # minimum total time needed 
        total_time = 0

        # edge cases
        colors = '1' + colors + '1'
        neededTime = [0] + neededTime + [0]

        # traverse list and pop balloons when same colors are adjacent to each other
        while right != len(colors) - 1:
            # check if pointers are pointing at the same color or not
            if colors[left] == colors[right]:
                # pop the one that requires lesser time
                if neededTime[left] < neededTime[right]:
                    total_time += neededTime[left]

                    colors = colors[:left] + colors[left+1:]
                    neededTime.pop(left)

                    # automatically moves ahead in the list
                else:
                    total_time += neededTime[right] 

                    colors = colors[:right] + colors[right+1:]
                    neededTime.pop(right)

            else: # if not, move on ahead
                left += 1
                right += 1
        
        # return minimum total time
        return total_time
        
