from collections import defaultdict


def containsDuplicate(nums) -> bool:
    return True if len(set(nums)) < len(nums) else False


def contains_dup(nums: list) -> bool:
    return True if len(set(nums)) < len(nums) else False


def contains_dup_hash(nums: list) -> bool:
    number_dict = defaultdict(int)
    for number in nums: 
        number_dict[number] += 1
        if number_dict[number] >1:
            return True
    return False


# # False
# print("false", contains_dup_hash(nums=[1, 2, 3, 4]))
# # True
# print("True", contains_dup_hash(nums=[1, 2, 3, 1]))









def contains_duplicate_prac(nums:list[int]) -> bool:
    return len(nums) != len(set(nums))

print(contains_duplicate_prac(nums=[1, 2, 3, 1]))