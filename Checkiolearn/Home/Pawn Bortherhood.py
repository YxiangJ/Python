'''
给定一个8*8的棋盘，同时给定8个棋子的位置。如果某一个棋子的位置可以由其他棋子一步到达，则认为该棋子安全。
判断8个棋子中安全的棋子的个数。如图所示，左边的安全棋子个数为6，右边的位1。
利用ord 和chr 转换求出该棋子左下和右下的棋子的位置坐标。如果该坐标在原来的集合中，则answer+1。最后返回answer
使用chr(ord(pawn[0]) + 1), chr(ord(pawn[0]) - 1)获得前后字母, ord相当于获得字母的数码(如ascii码), chr是逆过程
'''


def safe_pawns(pawns):
    answer = 0
    for pawn in pawns:
        if chr(ord(pawn[0]) - 1) + str(int(pawn[1]) - 1) in pawns or chr(ord(pawn[0]) + 1) + str(int(pawn[1]) - 1) in pawns:
            answer += 1
    return answer


def safe_pawns(pawns):
    al = [ord(d[0]) for d in pawns]
    num = [int(d[1]) for d in pawns]
    res = 0
    for i in range(len(pawns)):
        for k in range(len(pawns)):
            if al[i] == al[k] - 1 and num[i] == num[k] + 1 or al[i] == al[k] + 1 and num[i] == num[k] + 1:
                res += 1
                break
    return res
