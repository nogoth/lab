import random

arr = [ random.randint(-100,120) for x in range(1000) ]

def balancer(nums: list[int]) -> list(list[int]):
    # given an array partition it into two balanced sides, balanced defined as the sum of the elements
    # it's a two tail
    i = 0
    j = len(nums)-1
    lsum, rsum = nums[i], nums[j]
    while(i<j):
        if lsum < rsum:
            i += 1
            lsum += nums[i]
        elif lsum > rsum:
            j -= 1
            rsum += nums[j]
        else:
            # they are equal
            print() #break out dude
            i = j
    print(f" {i} left:{lsum} right:{rsum}")
    if lsum == rsum:
        return [ nums[:i], nums[i:] ]
    else:
        return []

print(f"{balancer([1,2,3,4])}")
print(f"{balancer([1,4,5])}")
print(f"{balancer(arr)}")
