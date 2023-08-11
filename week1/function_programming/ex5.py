from functools import reduce

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]


def sum_lists(*args):
    return reduce(lambda acc, numbers: sum(numbers) + acc, args, 0)

print(sum_lists(nums1, nums2, nums3))