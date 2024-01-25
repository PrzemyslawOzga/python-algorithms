import random

def get_random_list(
    size: int = 10, min_generated_val: int = 1, max_generated_val: int = 10
) -> list:
    unsorted_list = []
    for i in range(size):
        generated_num = random.randint(min_generated_val, max_generated_val)
        unsorted_list.append(generated_num)
    return unsorted_list
