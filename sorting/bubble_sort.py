from utilities.utils import get_random_list

def bubble_sort(array: list) -> list:
    cnt = len(array)
    while cnt > 0:
        for idx in range(1, cnt):
            first_checked_val = array[idx - 1]
            second_checked_val = array[idx]
            if first_checked_val > second_checked_val:
                array[idx - 1] = second_checked_val
                array[idx] = first_checked_val
        cnt = cnt - 1
    return array


if __name__ == "__main__":
    input_array = get_random_list()
    output_array = bubble_sort(input_array)
