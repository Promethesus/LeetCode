# The idea here is to save the number as the key and its index as the value
# then you check if the difference between target and number is in the dict
# if it is, return the index of the current number and the target index

# the key is number, Value is index, iterate through list 
# and check of the diff in in the dict, when you find it return



nums = [3,2,4]
target = 6


# def two_sum(nums:list[int], target:int)-> list[int]:
#     difference = {}

#     for index, number in enumerate(nums):
#         diff = target - number
#         if diff in difference:
#             return [index,difference[diff]]
#         difference[number] = index


# print(two_sum(nums,target))








nums = [3,2,4]
target = 6


def two_sum(nums:list[int], target:int)-> list[int]:
    values_dict = dict()

    for index, number in enumerate(nums):
        if (target - number) in values_dict:
            return [index , values_dict[target-number]]
        values_dict[number] = index

print(two_sum(nums,target))