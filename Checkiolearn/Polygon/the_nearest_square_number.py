# 用于数学分析


def nearest_square(number):
    # replace this for solution
    from math import sqrt
    s = int(sqrt(number))
    s1 = s ** 2
    s2 = (s + 1) ** 2
    return s2 if abs(s1 - number) >= abs(s2 - number) else s1


if __name__ == '__main__':
    print("Example:")
    print(nearest_square(8))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert nearest_square(8) == 9
    assert nearest_square(13) == 16
    assert nearest_square(24) == 25
    assert nearest_square(9876) == 9801
    print("Coding complete? Click 'Check' to earn cool rewards!")
