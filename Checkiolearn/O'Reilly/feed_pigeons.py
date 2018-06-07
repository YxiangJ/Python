# 这个任务说明了我们如何建模各种情况。当然，模型有一个有限的近似值，但通常我们不需要完美的模型。


def checkio(portions):
    i = 0
    nr = 0

    while portions > 0:
        i += 1
        if portions <= nr + i:
            return max(portions, nr)
        portions -= nr + i
        nr += i


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
