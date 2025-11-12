import random

def twosum(target: int, numbers: list[int]) -> list[int]:
    print(numbers)
    i = 0
    j = len(numbers)-1
    while(i<j):
        summy = numbers[i] + numbers[j]
        match summy:
            case _ if summy == target:
                return [i+1, j+1]
            case _ if summy < target:
                i += 1
            case _ if summy > target:
                j -= 1
            case _ if i == j:
                return []

def threesum(numbers: list[int]) -> list(list[int]): # and return a list of unique triples that result in sum 0 and are not the same cell repeated
    res = []
    numbers.sort()
#    print(numbers)
    for x in range(len(numbers)-2):
        print(f"  {x}  -v- {numbers[x]}")
        i = x+1
        if x > 0 and numbers[x] == numbers[x-1]:
#            print("continue")
            continue
        j = len(numbers)-1
        while(i<j):
            v = [numbers[x], numbers[i], numbers[j] ]
            print(f"{v}")
            if (numbers[i] + numbers[j] + numbers[x]) > 0:
                j -=1
            elif (numbers[i] + numbers[j] + numbers[x]) < 0:
                i += 1
            else:
                res.append(v)
                i += 1
                j -=1
                # lets go through and see if we've already worked the upcoming i ptr value again
                while i < j and numbers[i] == numbers[i-i]:
                    i +=1 #move past a prior done
                    print(f" pop  {i} {v}")
                # now i is sitting a unique new value let's check if we have worked a j with that i
                while i < j and numbers[j] == numbers[j+1]:
                    j -= 1
#                    print(f"{v} pop  {j} ")
    return res



arr = [ random.randint(-100,300) for x in range(10000) ]

print (threesum([0,0,0]))
print (threesum([0,1,1]))
print (threesum([-1,0,1,2,-1,4])) #should return -1 -1 2 and -1 0 1
#print (threesum(arr))
