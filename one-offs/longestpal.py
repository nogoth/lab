
class Solution:
    def longestPalindrome(self, s: str) -> str:
        fleft = -1
        rightmax=len(s) #-1 #maxleft is 0
        maxlength = -1
        
        #evens case
        for i in range(len(s)):
            left = i
            right = i

            while left >= 0 and right < rightmax and s[left] == s[right]:
                if right - left + 1 > maxlength:
                    maxlength = right - left + 1
                    fleft = left
                right += 1
                left -= 1

        #odds case
        for i in range(len(s)):
            left = i
            right = i+1

            while left >= 0 and right < rightmax and s[left] == s[right]:
                if right - left + 1 > maxlength:
                    maxlength = right - left + 1
                    fleft = left
                right += 1
                left -= 1

           
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


