from collections import Counter

def permutation_in_string(s1:str, s2:str)-> bool:
    s1_count = Counter(s1)

    for i in range(len(s2)):
        if s2[i] in s1_count:
            s1_count[s2[i]] -=1
        if i >= len(s1) and s2[i-len(s1)] in s1_count:
            s1_count[s2[i-len(s1)]] +=1
        if all(s1_count[i] == 0 for i in s1_count):
            return True
    return False

print(permutation_in_string("ab", "eidbaooo")) 



