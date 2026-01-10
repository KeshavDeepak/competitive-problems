class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st = []

        for ast in asteroids:
            if ast < 0: # moving left
                # simulate in st
                while True:
                    if not st:
                        st.append(ast)
                        break

                    if st[-1] < 0: # also moving left
                        st.append(ast)
                        break
                    
                    if st[-1] == abs(ast):
                        st.pop()
                        break
                    
                    if st[-1] > abs(ast):
                        break
                    
                    # st[-1] < abs(ast):
                    st.pop()
            else: # moving right
                st.append(ast)
        
        return st
    