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
        water = 0
        n = len(height)
        ans = [0] * n

        for x in range(1,n-1): #-1 the end can never hold water
            #sweep forward set the boxes to what it oculd be if the right side works out
            if height[x-1] < height[x]:
                ans[x] = height[x] - height[x-1]
            if height[x-1] > height[x]:
                ans[x] = height[x-1] - height[x]
        print(height)
        print(ans)
        for y in range(n-1, -1, -1):
            if ans[y] > 0:
                print(f"possible bucket at y {y} {ans[y]} {height[y]}")
                print(f"curr height :{height[y]} rightside: {height[y+1]}     {ans[y]}")
                if height[y] < height[y+1]:
                    ans[y] = 0

        return (sum(ans))







print( Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) )

print( Solution().trap([4,2,0,3,2,5]) )

#[0,1,0,2,1,0,1,3,2,1,2,1] == 6
