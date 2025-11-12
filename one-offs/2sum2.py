import random

class Solution:
    def twoSum(self, target: int, nums: list[int]) -> list[int]:
        print(nums)
        i = 0
        j = len(nums)-1
        while(i<j):
            summy = nums[i] + nums[j]
            match summy:
                case _ if summy == target:
                    return [i, j]
                case _ if summy > target:
                    print("i")
                    print(f" {i} {j} {summy} {target} {[nums[i],nums[j]]}")
                    i += 1
                case _ if summy < target:
                    print("j")
                    print(f" {i} {j} {summy} {target} {[nums[i],nums[j]]}")
                    j -= 1
                case _ if i == j:
                    print("exit")
                    return []


print (Solution().twoSum(9, [2,7,11,15])) # [0,1]
print (Solution().twoSum(6, [3,2,4])) # [1,2]
print (Solution().twoSum(6, [3,3])) # [1,2]
#print (Solution().twoSum(10, [1,2,3,4,6]))
#arr = [ random.randint(1,100) for x in range(100) ]
#arr.sort()
#print (Solution().twoSum(10, arr))
