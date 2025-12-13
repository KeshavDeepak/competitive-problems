class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # sort children & cookies
        g.sort()
        s.sort()

        # assign
        content = 0

        greed_i = 0
        cookies_i = 0

        while greed_i < len(g) and cookies_i < len(s):
            greed = g[greed_i]
            cookie = s[cookies_i]

            if greed <= cookie: # assign cookie to child
                content += 1
                greed_i += 1
            
            cookies_i += 1
        
        #
        return content
