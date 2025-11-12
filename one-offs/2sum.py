import random

class Solution:
    def twoSum(self, numbers: list[int],target: int) -> list[int]:
        i = 0
        j = len(numbers)-1
        while(i<j):
            summy = numbers[i] + numbers[j]
            if summy < target:
                i += 1
            elif summy == target:
                return [i+1, j+1]
            elif summy > target:
                j -= 1
        return []

arr = [ random.randint(1,100) for x in range(100) ]

arr.sort()

print (Solution().twoSum( [2,7,11,15],9))
