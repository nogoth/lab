import random
#in:  [1,0,-1,0,-2,2], target = 0
#out: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

   
def threesum(numbers: list[int], target=0) -> list(list[int]): # and return a list of unique triples that result in sum 0 and are not the same cell repeated
    res = []
    numbers.sort()
#    print(f" {target} {numbers}")

    for x in range(len(numbers)-2):
        i,j = x+1,len(numbers)-1
        if x > 0 and numbers[x] == numbers[x-1]:
            continue
        while(i<j):
            v = [numbers[x], numbers[i], numbers[j] ]
            if (numbers[i] + numbers[j] + numbers[x]) > target:
                j -=1
            elif (numbers[i] + numbers[j] + numbers[x]) < target:
                i += 1
            else:
                res.append(v)
                i += 1
                j -=1
                # lets go through and see if we've already worked the upcoming i ptr value again
                while i < j and numbers[i] == numbers[i-i]:
                    i +=1 #move past a prior done
                # now i is sitting a unique new value let's check if we have worked a j with that i
                while i < j and numbers[j] == numbers[j+1]:
                    j -= 1
    return res

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []
        # get all the triples that would + x == target
        for x in range(0, len(nums)-2):
#            print(nums[x:])
            ts = threesum(nums[x:], (target-nums[x]) )
            for threes in ts:
#                print(f"{threes} " )
                threes.insert(0,x)
                res.append( threes )


        return res
 


#arr = [ random.randint(-100,300) for x in range(10000) ]

#print (threesum([0,0,0]))
#print (threesum([0,1,1]))
#print (threesum([-1,0,1,2,-1,4])) #should return -1 -1 2 and -1 0 1
#print (threesum(arr,8))
print (Solution().fourSum([2,2,2,2], 8))
print (Solution().fourSum([1,0,-1,0,-2,2], 0))
print(" #out: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]] ")
#print (Solution().fourSum([1,0,-1,0,-2,2], 1))
#print (Solution().fourSum([1,0,-1,0,-2,2], 2))

