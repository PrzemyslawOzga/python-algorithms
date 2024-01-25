import pytest
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort

TEST_DATA = [[3, 1, 2, 4, 5], [-2, 1, 2, -1, 0], [5, 4, 3, 2, 1], [1, 1, 1, 1, 1, 1], [1, ]]

@pytest.mark.parametrize( "array", TEST_DATA)
def test_insertion_sort(array):
    expected_array = sorted(array)
    output_array = insertion_sort(array)
    assert expected_array == output_array

@pytest.mark.parametrize("array", TEST_DATA)
def test_bubble_sort(array):
    expected_array = sorted(array)
    output_array = bubble_sort(array)
    assert expected_array == output_array
