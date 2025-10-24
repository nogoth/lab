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
arr = [ random.randint(1,100) for x in range(100) ]

arr.sort()

print (twosum(10, [1,2,3,4,6]))
print (twosum(10, arr))
