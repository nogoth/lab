"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        ans = [0] * n

        left = [0] * n
        right = [0] * n

        max_height = -1
        for x in range(n):
            if max_height < height[x]:
                max_height = height[x]
            left[x] = max_height

        max_height = -1
        for x in range(n-1, -1, -1):
            if max_height < height[x]:
                max_height = height[x]
            right[x] = max_height
        for x in range(n):
            ans[x] = min(left[x], right[x]) - height[x]

        return (sum(ans))


print( Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) )
print( Solution().trap([4,2,0,3,2,5]) )

assert Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert Solution().trap([4,2,0,3,2,5]) == 9

#[0,1,0,2,1,0,1,3,2,1,2,1] == 6
