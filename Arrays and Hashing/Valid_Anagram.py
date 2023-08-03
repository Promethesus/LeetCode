


# s = "anagram"
# t = "nagarah"


# def isAnagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#     letter_count_s, letter_count_t = {}, {}

#     for i in range(len(s)):
#         # set the key to letter and value to 0
#         # if the key exist just add 1
#         letter_count_s[s[i]] = letter_count_s.get(s[i], 0) + 1
#         letter_count_t[t[i]] = letter_count_t.get(t[i], 0) + 1

#     for c in letter_count_s:
#         # the get protects against cause where we try to
#         # compare against something that doesnt exist
#         if letter_count_s[c] != letter_count_t.get(c, 0):
#             return False
#     return True


# s = "anagram"
# t = "anagram"



# def is_anagram(s:str, t:str)-> bool:
#     if len(s) != len(t):
#         return False
#     letter_count_s,letter_count_t = {}, {}

#     for i in range(len(s)):
#         letter_count_s[s[i]] = letter_count_s.get(s[i],0) +1
#         letter_count_t[t[i]] = letter_count_t.get(t[i],0) +1
#     for letter in s:
#         if letter_count_s[letter] != letter_count_t.get(letter,0):
#             return False
#     return True
         


# print(is_anagram(s, t))




# s = "anagram"
# t = "nagaram"


# def is_valid_anigram(s:str, t:str)-> bool:
#     if len(s) != len(t):
#         return False
#     letter_count_s, letter_count_t = {},{}

#     for index in range(len(s)):
#         letter_count_s[s[index]] = letter_count_s.get(s[index],0) + 1
#         letter_count_t[t[index]] = letter_count_t.get(t[index],0) + 1

#     for character in letter_count_s:
#         if letter_count_s[character] != letter_count_t.get(character):
#             return False 
#     return True
# print(is_valid_anigram(s,t))














s = "anagram"
t = "anagram"


def is_valid_anigram(s:str, t:str)-> bool:
    if len(s) != len(t):
        return False
    s_count, t_count = {}, {}

    for index in range(len(s)):
        s_count[s[index]] =s_count.get(s[index], 0) + 1
        t_count[t[index]] =t_count.get(t[index], 0) + 1
    
    for character in s_count:
        if s_count[character] != t_count.get(character, 0):
            return False
    return True

print(is_valid_anigram(s,t))