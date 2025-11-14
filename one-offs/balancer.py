import random
import sys

arr = [ random.randint(-100,120) for x in range(10) ]
# example given says take a file, read each line, it will be of a kind of each line = 1,2,3,4\n1,4,5\n
def balancer(nums: list[int]) -> list(list[int]):
    # given an array partition it into two balanced sides, balanced defined as the sum of the elements
    # preserve order however, numbers can be negative, it will fit all in memory, partitions will likely be differing lengths
    # it's a two tail
    print(f"**  ${nums}")
    i = 0
    j = len(nums)-1
    lsum, rsum = 0,0
    while i <= j :
#        print(f"STATS: lsum={lsum} {nums[i]} = {i}    -- {j} = {nums[j]} {rsum}=rsum")
        if lsum <= rsum:
            lsum += nums[i]
            i += 1
        else:
            rsum += nums[j]
            j -= 1
#    print(f"Final STATS: lsum={lsum} {nums[i]} = {i}    -- {j} = {nums[j]} {rsum}=rsum")

    if lsum == rsum: # 
        return [ nums[:i], nums[i:] ]
    else:
        return []

def validate_string(raw_string: str) -> bool:
    #define a class of items that are allowed
    #1-9,-,' '
    # could take the string, split it into each char and then uniq the compare, heavy lifting though
    # guess we can just iterate over the split and if it throws an error popout
    for val in raw_string.split(","): #granted we now have two splits... fix later
        try:
            v = int(val)
        except ValueError:
            return False
    return True

def turn_array(raw_string: str) -> list:
    if validate_string(raw_string):
        return [ int(x) for x in raw_string.split(",") ] 
    return []


def ponies():
    for x in sys.stdin:
        ar = turn_array(x)
        if ar:
    #        print(f"{balancer(ar) for _ if balancer(ar)}")
            balanced = balancer(ar)
            print(f"{balanced}" if balanced else "")

print(f"{balancer([1,3,4,1])}")
print(f"{balancer([1,2,3,4,2,1])}")
print(f"{balancer([1,2,3,5,0,1])}")
print(f"{balancer([1,2,3,4])}")
print(f"{balancer([1,4,5])}")
print(f"{balancer(arr)}")
print(f"{balancer([1,2,3,4,1,1])}")
print(f"{balancer([1,4,1,3,1])}")
print(f"{balancer([1,4,1,3,1])}")
print(f"{balancer([2,7,10,-1])}")
print(f"{balancer([2,7,10,19])}")

#- print(f"{turn_array('1,2,3,4,10,01,-1')}")
#- print(f"{turn_array('1')}")
#- print(f"{turn_array('1,a')}")
#- print(f"{turn_array('\n')}")


