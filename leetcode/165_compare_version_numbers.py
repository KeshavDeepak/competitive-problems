class Solution:
    def compareVersion(self, version1, version2):
        #* convert to lists
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        #* compare each corresponding revisions
        while version1 and version2:
            revision1 = int(version1[0])
            revision2 = int(version2[0])
            
            if revision1 > revision2: return 1
            if revision1 < revision2: return -1
            
            version1 = version1[1:]
            version2 = version2[1:]
        
        # if any version has remaining revisions and they are non-zero, it is later
        if version1:
            while version1:
                if int(version1[0]) != 0: return 1
                
                version1 = version1[1:]
                
        if version2:
            while version2: 
                if int(version2[0]) != 0: return -1
                
                version2 = version2[1:]
        
        # return 0 coz versions are identical
        return 0


# main code
solution = Solution()

# test cases
print(solution.compareVersion('1.2', '1.10')) 
print(solution.compareVersion('1.01', '1.001')) #<-- (solution, '1.01', '1.001')
print(solution.compareVersion('1.0', '1.0.0.0')) 
print(solution.compareVersion('7.5.2.4', '7.5.3')) 

        