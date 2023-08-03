# # Input: numbers = [2,7,11,15], target = 9
# # Output: [1,2]

# numbers = [2, 7, 11, 15]
# target = 9


# def two_sum(numbers: list, target: int) -> list:
#     l, r = 0, len(numbers)-1
#     sum = 0
#     while sum != target:
#         sum = sum(numbers[l], numbers[r])
#         if sum == target:
#             return [l + 1, r+1]
#         while sum < target:
#             l += 1
#         while sum > target:
#             r -= 1


# print(two_sum(numbers, target))


my_set = set()


print(my_set)
