

def characterReplacement(s:str, k:int)->int:
    count_dic = dict()
    l = 0 
    res = 0

    for r in range(len(s)):
        count_dic[s[r]] = count_dic.get(s[r], 0) +1
        
        while (r - l + 1) - max(count_dic.values()) > k:
            count_dic[s[l]] -= 1
            l +=1

        res = max(res, r-l+1)
    return res
        

print(characterReplacement('ABABADBABBBBBDBDB', 2))
