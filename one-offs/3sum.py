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

def threesum(numbers: list[int]) -> list(list[int]): # and return a list of triples that are not coequal and result in sum of 0
    # i != j , i != k, j != k
    res = []
    numbers.sort()
    print(numbers)
    for x in range(len(numbers)-2):
        print(f"  {x}  ")
        i = x+1
        if x > 0 and numbers[i] == numbers[x]:
            print("continue")
        j = len(numbers)-1
        while(i<j):
            print([numbers[x], numbers[i], numbers[j] ])
#            if numbers[x] == numbers[i] or numbers[x] == numbers[j]:
#                i+=1
#                j-=1
#                continue
# DO TWO TAIL. Ben. DUDE. 
            if (numbers[i] + numbers[j] + numbers[x]) > 0:
                j -=1
            elif (numbers[i] + numbers[j] + numbers[x]) < 0:
                i += 1
            else:
                res.append([numbers[x], numbers[i], numbers[j]] )
                i += 1
                j -=1
    return res



arr = [ random.randint(-100,100) for x in range(100) ]

#print (threesum([0,0,0]))
#print (threesum([0,1,1]))
print (threesum([-1,0,1,2,-1,4])) #should return -1 -1 2 and -1 0 1
#print (threesum(arr))
