


def longest_substring_no_repeat(s:str)-> int:
    longest_substring = 0
    sub_set = set()
    l = 0
    
    for r in range(len(s)):
        while s[r] in sub_set:
            sub_set.remove(s[l])
            l+=1
        sub_set.add(s[r])
        longest_substring = max(longest_substring, len(sub_set))
    return longest_substring


print(longest_substring_no_repeat("pwwkew"))




