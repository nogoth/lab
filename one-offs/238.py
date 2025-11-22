class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        ans[0] = 1
        for x in range(1,n):
            ans[x] = ans[x-1] * nums[x-1]
        tots = 1
        for x in range(n-1, -1, -1):
            ans[x] = ans[x] * tots
            tots = tots * nums[x]
        return ans 

print(Solution().productExceptSelf([1,2,3,4]))
assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]
#            print(f"x: {x}  -> {nums[x]}  {nums[x-1]}")
#            print(F"-- x: {x} num: {nums[x]} answer: {answer[x]} s: {seen} A: {answer[x] * seen}")
#            #print(F"then x: {x} num: {nums[x]} answer: {answer[x]} s: {seen} A: {answer[x] * seen}")
fee = list(range(1,3,1))
print(fee)
print(Solution().productExceptSelf(fee))
fee = list(range(1,2,1))
print(fee)
print(Solution().productExceptSelf(fee))
