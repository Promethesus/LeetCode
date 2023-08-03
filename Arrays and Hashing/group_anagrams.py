from collections import defaultdict


# def groupAnagrams(strs):
#     anagrams = defaultdict(list)

#     for word in strs:

#         count = [0] * 26
#         for character in word:
#             count[ord(character) - ord('a')] += 1

#         anagrams[tuple(count)].append(word)
#     return anagrams.values()







def groupAnagrams(strs:str)->list[str]:
    anagrams = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))
