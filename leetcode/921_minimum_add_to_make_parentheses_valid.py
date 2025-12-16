from collections import deque

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = deque([])

        for char in s:
            if char == '(':
                st.append(char)
            else: # char == ')'
                if st and st[-1] == '(': # match both and delete
                    st.pop()
                else: # string is not valid 
                    st.append(char)
        
        return len(st)
