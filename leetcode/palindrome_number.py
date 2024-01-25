# Leetcode #9
# Given an integer x, return true if x is a palindrome,
# and false otherwise.


def is_palindrome(num: int) -> bool:
    num_in_str = str(num)
    reversed_num_in_str_2 = "".join(reversed(num_in_str))
    if num_in_str == reversed_num_in_str_2:
        return True
    return False


if __name__ == "__main__":
    assert is_palindrome(121) is True
    assert is_palindrome(-121) is False
    assert is_palindrome(10) is False
    assert is_palindrome(1) is True
