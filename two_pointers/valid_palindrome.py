# A phrase is a palindrome if, after converting all uppercase letters
# into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.


# Found out python uses ASCII values under the hood so you can see if
# a character is between the two ASCII values by doing this comparison.
# This is assuming you arent allowed to use .isalnum()
def is_aphanumeric(character: str) -> bool:
    return ('a' <= character <= 'z' or
            'A' <= character <= 'Z' or
            '0' <= character < '9')


def is_palindrome(input: str) -> bool:
    l, r = 0, len(input) - 1
    while l < r:
        while l < r and not is_aphanumeric(input[l]):
            l += 1
        while l < r and not is_aphanumeric(input[r]):
            r -= 1
        if input[l].lower() != input[r].lower():
            return False
        l += 1
        r -= 1
    return True


print(is_palindrome("9,8"))
