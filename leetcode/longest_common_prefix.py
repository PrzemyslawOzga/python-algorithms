# Leetcode #14
# Write a function to find the longest common prefix 
# string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longest_common_prefix(array: list[str]) -> str:
    answer = ""
    array = sorted(array)
    first_word = array[0]
    last_word = array[-1]
    for i in range(min(len(first_word), len(last_word))):
        if first_word[i] != last_word[i]:
            return answer
        answer += first_word[i]
    return answer

if __name__ == "__main__":
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix([""]) == ""
