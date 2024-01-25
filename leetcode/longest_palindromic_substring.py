# Leetcode #5
# Given a string s, return the longest palindromic
# substring in s.

def longest_palindrome(s: str) -> str:
    if s == s[::-1]:
        return s

    output = ""


if __name__ == "__main__":
    assert longest_palindrome("babad") == "bab"
    assert longest_palindrome("cbbd") == "bb"
