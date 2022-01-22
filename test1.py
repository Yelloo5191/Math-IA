import cProfile, os, random

""" This is very bare-bones atm, mainly just for testing cProfile """

# O(n^2)
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# O(n)
def twoSum2(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i
    return []

def testTwoSum2():
    with open("sampleLarge.txt", "r") as f:
        text = f.read().split("\n")
        for x in text:
            listo = x[:-3].strip('][').split(', ')
            listo = list(map(int, listo))
            target = int(x[-1])
            print(twoSum2(listo, target))

cProfile.run("testTwoSum2()")

"""
Generating Test Cases:

with open("sampleLarge.txt", "w") as f:
    for x in range(10000):
        listo = []
        target = random.randint(0,40)
        for y in range(10):
            listo.append(random.randint(0,20))
        f.write(f"{listo} {target}\n")
"""