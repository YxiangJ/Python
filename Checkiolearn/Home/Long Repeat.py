#字符串中出现字母次数最多的次数

'''def long_repeat(x): return len(max([list(g) for k, g in __import__(
    'itertools').groupby(x)], key=len)) if x != '' else 0'''


# 分割线
def long_repeat(line):
    count = 1
    max = (len(line) >= 1)
    for i in range(len(line) - 1):
        if(line[i] == line[i + 1]):
            count += 1
            if count > max:
                max = count
        else:
            count = 1

    return max

# 分割线


'''def long_repeat(line):
    c = []
    if len(line) == 1:
        longest = 1
    else:
        for i in range(len(line) - 1):
            if line[i] != line[i + 1]:
                c.append(1)
            elif i == 0:
                c.append(1)
                c[-1] += 1
            else:
                c[-1] += 1
            i += 1
        if len(c) == 1:
            longest = c[0]
        elif len(c) == 0:
            longest = 0
        else:
            longest = max(c)
    return longest'''

# 分割线


'''def long_repeat(line):
    maxv = count = 0
    last = None
    for c in line:
        if c == last:
            count += 1
        else:
            maxv = max(maxv, count)
            count = 1
            last = c
    return max(maxv, count)
'''

# 分割线
'''from itertools import groupby


def long_repeat(line):
    if len(line) > 0:
        return len(sorted([''.join(x) for z, x in groupby(line)], key=len)[-1])
    else:
        return 0'''


# 分割线
'''import numpy as np


def long_repeat(line):
    if len(line) < 2:
        return len(line)
    arr = np.array(bytearray(line, 'utf-8'))
    changes = np.argwhere(arr[:-1] != arr[1:])
    if changes.shape[0] == 0:
        return len(line)
    return int(np.diff(changes, axis=0).max())'''


# 分割线
'''import re


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here

    longest = 0

    for letter in set(line):
        for match in re.findall(f"[{letter}]+", line):
            if len(match) > longest:
                longest = len(match)

    return longest'''


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
