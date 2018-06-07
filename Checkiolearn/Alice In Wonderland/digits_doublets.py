# 这个任务就像查找数字一样。它显示了这个世界上有多少事物可以用数学，甚至文字来表示。


def checkio(numbers):
    paths = [[numbers[0]]]
    while True:
        p = paths.pop(0)
        for c in set(numbers) - set(p):
            if sum(x != y for x, y in zip(str(p[-1]), str(c))) == 1:
                if c == numbers[-1]:
                    return p + [c]
                paths.append(p + [c])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [
        123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [
        111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [
        456, 454, 654], "Third, [456, 656, 654] is correct too"
