# Given an integer array nums and an integer k,
# return the k most frequent elements.
# You may return the answer in any order.


# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]


# def topKFrequent(nums, k):
#     freq = {}
#     for number in nums:
#         increment = freq.get(number, 0)
#         increment += 1
#         freq[number] = increment
#     sorted_numbers = sorted(freq.items(), key=lambda x: x[1], reverse=True)
#     highest_freq = [key for key, value in sorted_numbers[:k]]
#     return highest_freq


# print(topKFrequent([1, 1, 1, 2, 2, 3], 3))

























def topKFrequent(nums, k):
    count_dict = dict()

    for number in nums: 
        count_dict[number] = count_dict.get(number,0) +1

    sorted_numbers = sorted(list(count_dict.keys()))
    print(sorted_numbers)
    top_k = sorted_numbers[:k]

    return top_k



print(topKFrequent([4,1,-1,2,-1,2,3], 2))




