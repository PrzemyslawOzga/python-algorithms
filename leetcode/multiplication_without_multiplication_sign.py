# Own algorithm from first interview. Write
# function to multiple two numbers, but you
# can't use multiple sign

def multiple(x: int, y: int) -> int:
    lower_value = x
    higher_value = abs(y)
    if x > y:
        higher_value = abs(x)
        lower_value = y

    answer = 0
    for _ in range(higher_value):
        answer += lower_value

    if lower_value < 0 and lower_value % 2 == 0:
        answer = -answer
    return answer


if __name__ == "__main__":
    assert multiple(3, 3) == 9
    assert multiple(-3, -3) == -9
    assert multiple(-3, 3) == -9
    assert multiple(3, -3) == -9
    assert multiple(2, -2) == 4
    assert multiple(2, -2) == 4
    assert multiple(0, 2) == 0
