# Leetcode #3
# Given a string s, find the length of the longest
# substring without repeating characters.

def length_of_longest_substring(word: str) -> int:
    start = max_length = 0
    used = {}
    for idx, unique_char in enumerate(word):
        if unique_char in used and start <= used[unique_char]:
            start = used[unique_char] + 1
        else:
            max_length = max(max_length, idx - start + 1)
        used[unique_char] = idx
    return max_length


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("dupa") == 4
