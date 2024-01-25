# Leetcode #4
# Given two sorted arrays nums1 and nums2 of size m and n
# respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
import math
from typing import List


def find_median_sorted_arrays(arr1: List[int], arr2: List[int]) -> float:
    merged_array = arr1 + arr2
    merged_array.sort()
    median = _calculate_median(merged_array)

    return median


def _calculate_median(merged_array: List[int], median: int = None) -> float:
    middle_of_array = (len(merged_array) - 1) / 2
    if isinstance(middle_of_array, int):
        median = merged_array[middle_of_array]
    if isinstance(middle_of_array, float):
        median = (
            merged_array[math.floor(middle_of_array)]
            + merged_array[math.ceil(middle_of_array)]
        ) / 2

    return median


if __name__ == "__main__":
    assert find_median_sorted_arrays([], [1]) == 1
    assert find_median_sorted_arrays([], [1, 2]) == 1.5
    assert find_median_sorted_arrays([1, 3], [2]) == 2
    assert find_median_sorted_arrays([1, 4], [2, 3, 5, 6]) == 3.5
