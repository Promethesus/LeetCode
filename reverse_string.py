test_string = 0


def reverse_string(input_string: str) -> str:
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    reversed_string = input_string[::-1]
    return reversed_string


print(reverse_string(test_string))
