import cProfile, os, random

""" This is very bare-bones atm, mainly just for testing cProfile """
# TODO: Write n^3 and log(n) methods

# O(n^3)
def twoSum(nums: list, target: int) -> list:
    pass

# O(n^2)
def twoSum1(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# O(n)
def twoSum2(nums: list, target: int) -> list:
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i
    return []

# O(log(n))
def twoSum3(nums: list, target: int) -> list:
    nums.sort()
    mid = len(nums) // 2

    while True:
        if nums[mid] > target - nums[mid - 1]:
            nums = nums[mid:]
        elif nums[mid] < target - nums[mid - 1]:
            nums = nums[:mid+1]
        else:
            return [nums[mid], target - nums[mid]]
    return []


# Method to be measured
def testTwoSum(twoSum: callable, file: str) -> None:
    with open(file, "r") as f:
        text = f.read().split("\n")
        for x in text:
            listo = x[:-3].strip('][').split(', ')
            listo = list(map(int, listo))
            target = int(x[-1])
            print(twoSum(listo, target))

cases = [
    [
        ("sampleSmall.txt", twoSum),
        ("sampleMedium.txt", twoSum),
        ("sampleLarge.txt", twoSum),
        ("sampleExtraLarge.txt", twoSum)
    ],
    [
        ("sampleSmall.txt", twoSum1),
        ("sampleMedium.txt", twoSum1),
        ("sampleLarge.txt", twoSum1),
        ("sampleExtraLarge.txt", twoSum1)
    ],
    [
        ("sampleSmall.txt", twoSum2),
        ("sampleMedium.txt", twoSum2),
        ("sampleLarge.txt", twoSum2),
        ("sampleExtraLarge.txt", twoSum2)
    ],
    [
        ("sampleSmall.txt", twoSum3),
        ("sampleMedium.txt", twoSum3),
        ("sampleLarge.txt", twoSum3),
        ("sampleExtraLarge.txt", twoSum3)
    ],
]

# Profile run times
for case in cases:
    for test in case:
        cProfile.run(f"testTwoSum({test[1]},{test[0]})")

"""
Generating Test Cases:

with open("sampleSmall.txt", "w") as f:
    for x in range(100):
        listo = []
        target = random.randint(0,20)
        for y in range(10):
            listo.append(random.randint(0,10))
        f.write(f"{listo} {target}\n")

with open("sampleMedium.txt", "w") as f:
    for x in range(1000):
        listo = []
        target = random.randint(0,40)
        for y in range(10):
            listo.append(random.randint(0,20))
        f.write(f"{listo} {target}\n")

with open("sampleLarge.txt", "w") as f:
    for x in range(10000):
        listo = []
        target = random.randint(0,40)
        for y in range(10):
            listo.append(random.randint(0,20))
        f.write(f"{listo} {target}\n")
"""