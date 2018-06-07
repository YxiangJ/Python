# 这个任务向你介绍概率论和统计学的基础知识。有趣的事实：不管初始状态如何，随着步骤数的增加，概率接近0.5！


from collections import defaultdict


def checkio(marbles, step):
    swap = str.maketrans("bw", "wb")

    pattern_counts = {"".join(sorted(marbles)): 1}
    for i in range(step - 1):
        next_pattern_counts = defaultdict(int)
        for marbles, count in pattern_counts.items():
            for i in range(len(marbles)):
                swapped = marbles[:i] + \
                    marbles[i].translate(swap) + marbles[i + 1:]
                next_pattern_counts["".join(sorted(swapped))] += count
        pattern_counts = next_pattern_counts

    w_count = sum([marbles.count("w") * count for marbles,
                   count in pattern_counts.items()])
    return round(w_count / len(marbles)**(step), 2)

'''
import numpy as np

def checkio(marbles, step):
    n, w = len(marbles), marbles.count('w')
    
    p = np.zeros(n + 1)
    p[w] = 1

    pw = np.linspace(0, 1, n + 1)
    pb = np.linspace(1, 0, n + 1)

    for _ in range(step - 1):
        p = np.roll(p*pw, -1) + np.roll(p*pb, 1)
    return round(float(sum(p*pw)), 2)
'''

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    print ("well done!")
