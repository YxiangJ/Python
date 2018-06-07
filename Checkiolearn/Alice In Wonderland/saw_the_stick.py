'''
在这个任务中，你将学习三角数字。三角形数字或三角形数字形成等边三角形的物体。这是一个有趣的序列，它有各种应用。
这是一个真实世界的应用程序：在使用循环赛小组赛的比赛形式中，需要在n个小组之间进行比赛的次数等于三角形数Tn-1。
例如，有4支球队的小组赛需要6场比赛，而有8支球队的小组赛需要28场比赛。
'''


def checkio(number):
    triangles = [n * (n + 1) // 2 for n in range(1, 32)]
    # 31st+32nd triangular > max number
    for a in range(32):
        for b in reversed(range(32)):
            if sum(triangles[a:b]) == number:
                return triangles[a:b]
    return []


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
