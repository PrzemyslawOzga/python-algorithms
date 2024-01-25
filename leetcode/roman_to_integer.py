# Leetcode #13
# Roman numerals are represented by seven different
# symbols: I, V, X, L, C, D and M. For example, 2 is
# written as II in Roman numeral, just two ones added
# together. 12 is written as XII, which is simply X + II.
# The number 27 is written as XXVII, which is XX + V + II.


def roman_to_int(roman_str: str) -> int:
    dictionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    output = 0
    i = 0
    while i < len(roman_str):
        if i < len(roman_str) - 1:
            if roman_str[i] + roman_str[i + 1] in dictionary:
                output += dictionary[roman_str[i] + roman_str[i + 1]]
                i += 2
            else:
                output += dictionary[roman_str[i]]
                i += 1
        else:
            output += dictionary[roman_str[i]]
            i += 1
    return output


if __name__ == "__main__":
    assert roman_to_int("III") == 3
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994
