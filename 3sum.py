nums = [-1,0,1,2,-1,-4]


def threesum(nums:list[int]) -> list[int]: 
    res = []
    nums.sort()
    
    for index, number in enumerate(nums):
        if index > 0 and number == nums[index-1]:
            continue
        l,r = index+1, len(nums)-1
        while l < r: 
            the_sum = number + nums[l]+ nums[r]
            if the_sum > 0:
                r -= 1
            elif the_sum < 0:
                l+= 1
            else:
                res.append([number, nums[l],nums[r]])
                l+=1
                while nums[l] == nums[l-1] and l < r: 
                    l+=1
    return res


print(threesum(nums))