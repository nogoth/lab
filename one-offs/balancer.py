import random
import sys

arr = [ random.randint(-100,120) for x in range(10) ]
# example given says take a file, read each line, it will be of a kind of each line = 1,2,3,4\n1,4,5\n
def balancer(nums: list[int]) -> list(list[int]):
    # given an array partition it into two balanced sides, balanced defined as the sum of the elements
    # preserve order however, numbers can be negative, it will fit all in memory, partitions will likely be differing lengths
    # HINT: it's a two tail
#    print(f"**  ${nums}")
    if not nums: #there is a bug somewhere in turn_array if you pass it 'foo\n'
        return []
    i = 0
    j = len(nums)-1
    lsum, rsum = 0,0
    while i <= j :
#        print(f"STATS: lsum={lsum} val:{nums[i]} = i:{i}    -- j:{j} = val:{nums[j]} {rsum}=rsum")
        if lsum <= rsum:
            lsum += nums[i]
            i += 1
        else:
            rsum += nums[j]
            j -= 1
#    print(f"Final STATS: lsum={lsum} left:{i}    -- right:{j} {rsum}=rsum")

    if lsum == rsum and nums[i:]: # 
        # [[-10, 1, -8, 10, -5, -2, 9, -5, 0, 10], []] was valid because [0] == [0] but no
        return [ nums[:i], nums[i:] ]
    else:
        return []
#
# give a list of strings if they are all integers return true
#   otherwise the first failure, just say False and we can move on
# -- 
def valid_integer_list(stringsList: list) -> bool:
    for val in stringsList:
        try:
            v = int(val)
        except ValueError:
            return False
    return True

def turn_array(raw_string: str) -> list:
    # TODO: needs logic to protect against "1,2,3,4,"
    ta_array = raw_string.split(",")
    if valid_integer_list(ta_array):
        return [ int(x) for x in ta_array ] 
    return []


def read_stdin_output_balanced():
    for x in sys.stdin:
        ar = turn_array(x)
        if ar:
            balanced = balancer(ar)
            print(f"{balanced}" if balanced else "")

def test_items():
    print(f"{balancer([0, -8, -6, 0, 1, 5, 10, 2, 0, 4])}")
    return

    # [[-10, 1, -8, 10, -5, -2, 9, -5, 0, 10], []]
    # 
    print(f"{balancer([-10, 1, -8, 10, -5, -2, 9, -5, 0, 10])}")
    return 
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

    # test to make sure that turn array handles at least some lined that could happen in the input
    assert turn_array("\n") == [], "strange spaced characters made an array" 
    assert turn_array("1,a") == [], "arrays that have characters made an integer array"
    assert turn_array("1") == [1], "single element didn't create a single element array"
    assert turn_array('1,2,3,4,10,01,-1') == [1,2,3,4,10,1,-1], "Normal Array creation failed to work"


def open_file_output():
    with open("integer.lists", 'r') as ilf:
        for entry in ilf:
            ta = turn_array(entry)
            balanced = balancer(ta)
            sys.stderr.write(f"balancer: {balanced} ta:{ta}\n" )
            sys.stdout.write(f"{balanced}\n" if balanced else "")

test_items()
