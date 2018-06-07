#数组中偶数和与最后一位数相乘结果

def checkio(array):
    sum = 0
    if array:
        for i in range(len(array)):
            if not (i % 2):
                sum += array[i]
        return sum * array[-1]
    else:
        return 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
