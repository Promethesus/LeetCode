# Given an unsorted array of integers nums,
# return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


def longestConsecutive(nums) -> int:
    largest_run = 0
    number_set = set(nums)

    for number in number_set:
        if (number - 1) not in number_set:
            current_run = 0
            while (number + current_run) in number_set:
                current_run += 1
            largest_run = max(largest_run, current_run)
        return largest_run


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))
