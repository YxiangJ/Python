'''
在这里，您将学习如何使用布尔值和运算符。你甚至可以考虑数字作为布尔值
"conjunction"和, "disjunction"或, "implication"包含, "exclusive"异或, "equivalence"等
'''
OPERATION_NAMES = ("conjunction", "disjunction",
                   "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if operation == 'conjunction':
        return x & y
    if operation == 'disjunction':
        return x | y
    if operation == 'implication':
        return (not x) | y
    if operation == 'exclusive':
        return x ^ y
    if operation == 'equivalence':
        return x == y


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
    print("well done")
