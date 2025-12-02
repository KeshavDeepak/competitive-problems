class Solution:
    def findPages(self, arr, k):
        # base case
        if len(arr) < k: return -1
        
        # main cases
        max_pages = arr[0]
        total = 0
        
        for pages in arr:
            max_pages = max(max_pages, pages)
            total += pages
        
        left = max_pages
        right = total
        answer = 0
        
        while left <= right:
            target_pages = (left + right) // 2
            students = 0
            curr_bucket = 0
            
            for pages in arr:
                if curr_bucket + pages <= target_pages:
                    curr_bucket += pages
                else:
                    students += 1
                    curr_bucket = pages
            
            # for the last bucket
            students += 1
            
            if students <= k: # possible to reach target_pages, try for lower
                answer = target_pages
                right = target_pages - 1
            else: # not possible, try for higher
                left = target_pages + 1
        
        return answer
