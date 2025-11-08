class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        st = [(len(temperatures)-1, temperatures[-1])]        

        for index in range(len(temperatures)-1, -1, -1):
            # find first warmer temperature from stack
            while st:
                if st[-1][1] <= temperatures[index]:
                    st.pop()
                else:
                    break
            
            # update answer
            answer[index] = 0 if not st else (st[-1][0] - index)

            # update stack
            st.append((index, temperatures[index]))

        return answer

