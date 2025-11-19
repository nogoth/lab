"""
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""



from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # short circuit since we can't ever not send "" in this case
        if len(s) < len(t):
            return ""

        minLeft = -1
        minLength = len(s)+1
        left = 0 
        required = len(t)
        tc = Counter(t)
        ## logic
        for  right, val in enumerate(s):
            tc[val] -= 1
            if tc[val] >= 0:
                required -= 1
            while required == 0: #we found a subset
                if right - left +1 < minLength:
                    minLength = right - left + 1 
                    minLeft = left
                tc[s[left]] += 1
                if tc[s[left]] > 0: #meaning we needed ii
                    required += 1

                left += 1
        ## /logic
        print( s[minLeft:minLeft + minLength ] )

        return "" if minLeft < 0 else s[minLeft:minLeft + minLength ] 

print(Solution().minWindow("ADOBECODEBANC","ABC") )
assert Solution().minWindow("ADOBECODEBANC","ABC") == "BANC"
assert Solution().minWindow("AAAAAAAAAAAA","AA") == "AA"
assert Solution().minWindow("AAAAAABAAbAA","Ab") == "Ab"
assert Solution().minWindow("a","aa") == ""
assert Solution().minWindow("a","a") == "a"
