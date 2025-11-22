
class Solution:
    def longestPalindrome(self, s: str) -> str:
        fright, fleft = -1,-1
        rightmax=len(s) #-1 #maxleft is 0
        maxlength = -1
        
        for i,val in enumerate(s):
            left=i
            right=i

            while left > -1 and right < rightmax:
                if s[left] == s[right]:
                    if right - left + 1 > maxlength:
                        maxlength = right - left + 1
                        fleft = left
                    right += 1
                else: #left char != right char, reduce left
                    left -= 1
#            print(f"maxlegnth {maxlength} fleft {fleft}")
            
        return f"{s[fleft:fleft + maxlength]}"


print(Solution().longestPalindrome("aacabdkacaa")) # aca
print(Solution().longestPalindrome("cbbd")) # bb
print(Solution().longestPalindrome("babad")) # bab
print(Solution().longestPalindrome("noon")) # noon
print(Solution().longestPalindrome("nooon")) # nooon
print(Solution().longestPalindrome("noobs")) # oo
print(Solution().longestPalindrome("boobs")) # boob
print(Solution().longestPalindrome("sboobs")) # sboobs
print(Solution().longestPalindrome("barx")) # "b"


