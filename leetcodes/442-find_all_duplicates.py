def findduplicates(nums: list[int]) -> list[int]:
    d: dict = {}

    for b in nums:
        if b not in d:
            d[b] = 1
        else:
            d[ b ] += 1
    return list(filter(lambda x: d[x] > 1, d) )

print(findduplicates([1,2,2,3,3,4,1]))
