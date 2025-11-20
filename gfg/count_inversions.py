class Solution:
    def mergesort(self, arr, left, right):
        # --- base case
        if left == right: return [arr[left]], 0
        
        # --- recursive case
        mid = (left + right) // 2
        left_arr, left_ans = self.mergesort(arr, left, mid)
        right_arr, right_ans = self.mergesort(arr, mid+1, right)
        
        # merge left and right arrays
        i = 0
        j = 0
        ans = 0
        arr_sorted = []
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] > right_arr[j]:
                arr_sorted.append(right_arr[j])
                j += 1
                
                ans += (len(left_arr)-i)
            else:
                arr_sorted.append(left_arr[i])
                i += 1
        
        # if any leftover values in either array, add them
        if i < len(left_arr):
            arr_sorted.extend(left_arr[i:])
        
        if j < len(right_arr):
            arr_sorted.extend(right_arr[j:])
        
        #
        # print(arr_sorted, ans, left, right)
        return arr_sorted, ans + left_ans + right_ans
            
            
    
    def inversionCount(self, arr):
        # Code Here
        _, ans = self.mergesort(arr, 0, len(arr)-1)
        
        return ans
        
        
        
