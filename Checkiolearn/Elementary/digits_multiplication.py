# 一组数除0外的每个数字相乘


def checkio(number):
    result = 1
    s = str(number)
    for i in s:
        if int(i):
            result *= int(i)

    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
