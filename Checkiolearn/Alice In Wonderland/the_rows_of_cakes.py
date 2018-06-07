# 这是一个图像和模式识别的例子。这个概念可以用于游戏机制，或者如果你想写一个游戏机器人，或者将打印文本转换为数字格式。


def checkio(cakes):
    lines = []
    for i in range(0, len(cakes) - 2):
        for j in range(i + 1, len(cakes) - 1):
            counter = 0
            for elem in lines:
                if cakes[i] in elem and cakes[j] in elem:
                    counter += 1
            if counter == 0:
                combi = [cakes[i], cakes[j]]
                for k in range(j + 1, len(cakes)):
                    if (cakes[j][0] - cakes[i][0]) * (cakes[k][1] - cakes[i][1]) == (cakes[j][1] - cakes[i][1]) * (cakes[k][0] - cakes[i][0]):
                        combi.append(cakes[k])
                if len(combi) >= 3:
                    lines.append(combi)
    return len(lines)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
