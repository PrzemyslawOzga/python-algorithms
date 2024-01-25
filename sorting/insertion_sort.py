from utilities.utils import get_random_list

def insertion_sort(array: list) -> list:
    for second_idx in range(1, len(array)):
        first_idx = second_idx - 1
        while first_idx >= 0 and array[second_idx] < array[first_idx]:
            array[first_idx + 1] = array[first_idx]
            first_idx = first_idx - 1
        array[first_idx + 1] = array[second_idx]
    return array


if __name__ == "__main__":
    input_array = get_random_list()
    output_array = insertion_sort(input_array)
