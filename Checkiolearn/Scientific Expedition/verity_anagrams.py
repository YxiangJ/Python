def capture(matrix):
    n = len(matrix)
    p = []
    m = []  # 感染状态
    q = []
    for i in range(n):
        m.append(False)  # 计算机初始状态是/否会感染
    for i in range(n):
        p.append(matrix[i][i])  # 计算机初始防御

    while (sum(p) != 0):
        t = 1000000
        for i in range(n):
            m[i] = False
        for i in range(n):
            if (p[i] == 0):
                for j in range(n):
                    if (matrix[i][j] == 1 and p[j] != 0):
                        m[j] = True  # 只要有感染源连接，感染状态变为是
                        if (p[j] < t):
                            t = p[j]  # 任意一台计算机防御变为0需要的最小时间
        for i in range(n):
            if (m[i] == True):
                p[i] = p[i] - t  # 根据感染状态以及最小时间刷新
        q.append(t)
    return sum(q)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
    print("Well, You can check it!")
