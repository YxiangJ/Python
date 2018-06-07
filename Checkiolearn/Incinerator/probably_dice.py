'''
这个任务说明了概率的一些基本知识。
许多事件可以被描述为其他事件的组合。在这种情况下，你将几个骰子组合成一个整体来暴击兽人王的巨大伤害。
'''

from math import pow, factorial


def choose(a, b):
    if b == 0 or a == b:
        return 1
    else:
        numer = factorial(a)
        denom = factorial(b) * factorial(a - b)
        return numer // denom


def probability(dice_number, sides, target):
    k_max = (target - dice_number) // sides
    try:
        return sum(pow(-1, k) * choose(dice_number, k) * choose(target - sides * k - 1, dice_number - 1) for k in
                   range(0, k_max + 1)) / pow(sides, dice_number)
    except ValueError:
        return 0


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)
           ), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)
           ), "Many dice, many sides"
    print("well done!")
