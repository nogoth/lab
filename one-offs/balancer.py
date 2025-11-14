import random

arr = [ random.randint(-100,120) for x in range(1000) ]
# example given says take a file, read each line, it will be of a kind of each line = 1,2,3,4\n1,4,5\n
def balancer(nums: list[int]) -> list(list[int]):
    # given an array partition it into two balanced sides, balanced defined as the sum of the elements
    # preserve order however, numbers can be negative, it will fit all in memory, partitions will likely be differing lengths
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

#print(f"{balancer([1,2,3,4])}")
#print(f"{balancer([1,4,5])}")
#print(f"{balancer(arr)}")

#- print(f"{turn_array('1,2,3,4,10,01,-1')}")
#- print(f"{turn_array('1')}")
#- print(f"{turn_array('1,a')}")
#- print(f"{turn_array('\n')}")


def dontdothis():
    import sys

    for x in sys.stdin:
        print(f"{x.strip()}")
