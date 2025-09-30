import random

def quicksort(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        pivot = array[0]  # lets go with the front but i could do -1
        leftside = [x for x in array[1:] if x < pivot]  # capture the values less than x
        rightside = [
            x for x in array[1:] if x >= pivot
        ]  # everything on right is bigger than
        return (
            quicksort(leftside) + [pivot] + quicksort(rightside)
        )  # return partially sorted array (which will be recursed into with a smaller and smaller set of values to sort


def randArray(min: int = 1, max: int = 20, size: int = 20) -> list:
    return [random.randint(min, max) for _ in range(size)]

#
#  Original way i thought of counting duplicates
#
def count_duplicates(array: list) -> list:
    our_array = quicksort(array)
    y = our_array[0]
    stack = []
    count = 1  # not zero, cause we've now seen it once
    for x in our_array[1:]:
        if x == y:
            count = count + 1
        else:
            stack.append((y, count))
            y = x
            count = 1
    stack.append((y, count)) # add the final tuple in
    return stack

#
# attempt to do a functional programming version of it
#
def f_count_duplicates(array: list) -> list:
    uniques = sorted(list(set(array)))
    # if we were to do, uniques.sort() then it isn't functional anymore. It has a mutation to make it a sort. 

    return [ (x, array.count(x)) for x in uniques] 


def unzip_tuples(tuple_array: list) -> list: # i need to figure out how to flatten() the list afterwards
    return [ [x] * y for (x,y) in tuple_array ] 
    

#
# fisher yates shuffle, i think
#
def f_y_shuff(arr: list) -> list:
    # remember there are no for(x=0;x<10;x++) in python3 native
    print(f"f_y_1: {arr}")
    for i in range(len(arr)):
        for j in range(len(arr) - i):
            if (i < j):
                p = random.randint(i,j)
                arr[i], arr[p] = arr[p], arr[i]
    print(f"f_y_2: {arr}")
    return arr


if __name__ == "__main__":
    our_list = randArray(size=100)
    print(our_list)
    print(quicksort(our_list))
    print(our_list)
    print(count_duplicates(our_list))
    print(f"{f_count_duplicates(our_list)} duplicates")
    print(unzip_tuples(count_duplicates(our_list)))
    print(f_y_shuff(our_list[::-1]))
