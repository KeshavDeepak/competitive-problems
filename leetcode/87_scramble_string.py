class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        self.dp = {}

        def f(s1, s2): # true if s1 can become s2, false if not 
            # base cases
            if s1 == s2: 
                return True
            
            if len(s1) == 1: # no more recursion possible
                return False
            
            # -- already memoized? use it
            if (s1, s2) in self.dp:
                return self.dp[(s1, s2)]

            if sorted(s1) != sorted(s2): # char freqs dont match, not possible
                return False
            
            # recursive case
            # -- split at every index and recurse
            answer = False

            for index in range(1, len(s1)):
                left_s1 = s1[:index]
                left_s2 = s2[:index]

                right_s1 = s1[index:]
                right_s2 = s2[index:]

                pair_left_s2 = s2[-index:]
                pair_right_s2 = s2[:-index]

                # recurse and check if both halves can reach their respective mini s2s
                if f(left_s1, left_s2) and f(right_s1, right_s2):
                    answer = True
                    break
                
                # else also recurse to check if both halves can reach the opposite pairing of s2s
                if f(left_s1, pair_left_s2) and f(right_s1, pair_right_s2):
                    answer = True
                    break
                
            # memoize
            self.dp[(s1, s2)] = answer

            return answer

        return f(s1, s2) 
