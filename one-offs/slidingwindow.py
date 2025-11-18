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

        tCounter = Counter(t) # sets a dict up with the required chars keys , val = 0

        left = 0 
        minLeft = -1 #or float('inf')

        wanted = len(t) # how many characters we want
        minLength = len(s) + 1 # if we return it'll be at most all of S

        # use right as the value in the enumerate
        for right, val in enumerate(s):
            tCounter[val] -= 1
            if tCounter[val] >= 0:
                wanted -= 1
            print(f"val:{val} tval:{tCounter[val]} wanted:{wanted}")
            while wanted == 0:
                # oh hey, is our window smaller than the curr minlength windowsize placeholder?
                if right - left + 1 < minLength:
                    minLeft = left # make minLeft be current left
                    minLength = right - left + 1 # update to new minimum size
                    print(f"ml:{minLeft} window:{minLength}")
                tCounter[ s[left] ] += 1
                if tCounter[ s[left] ] > 0:
                    wanted +=1
                left += 1
            print(f"ml:{minLeft} window:{minLength}")

        print(tCounter)

        return "" if minLeft < 0 else s[minLeft:minLeft + minLength ] 

assert Solution().minWindow("ADOBECODEBANC","ABC") == "BANC"
assert Solution().minWindow("AAAAAAAAAAAA","AA") == "AA"
assert Solution().minWindow("AAAAAABAAbAA","Ab") == "Ab"
assert Solution().minWindow("a","aa") == ""
assert Solution().minWindow("a","a") == "a"
