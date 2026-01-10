class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        st = []
        hash = {}

        for num in nums2:
            # find place in st and push
            while st:
                if num > st[-1]: # pop and save
                    num1 = st.pop()
                    hash[num1] = num
                else:
                    break
            
            st.append(num)
        
        answer = [hash.get(num, -1) for num in nums1]

        return answer
    