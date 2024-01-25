# Leetcode #1
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add
# up to target. You may assume that each input would
# have exactly one solution, and you may not use the same
# element twice. You can return the answer in any order.
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    for num in range(len(nums)):
        checked_num = target - nums[num]
        if checked_num in nums and nums.index(checked_num) != num:
            return [num, nums.index(checked_num)]


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 22) == [1, 3]
