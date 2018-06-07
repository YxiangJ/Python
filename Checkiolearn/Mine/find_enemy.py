#基于六角网格的战争游戏设计


import math
def find_enemy(y, d, e):
    #把符号转换成位置
    y = genPos(y)
    e = genPos(e)
    
    #计算最大距离
    dist = max([abs(y[0]-e[0]),abs(y[1]-e[1])])
    if abs(y[0]-e[0]) == round(abs(y[1]-e[1])):
        dist += 1
        
    #根据自己的方向对角度计算的直线进行修正
    if d == 'NE' or d== 'SW':
        xP = 1
        yP = -1.5
    if d == 'NW' or d== 'SE':
        xP = 1
        yP = 1.5
    if d == 'N' or d== 'S':
        xP = 1
        yP = 0
        
    #算出自己的真横和敌人的角度
    dig = culcDegrees([y[0]+xP,y[1]+yP], y, e)
    
    #从角度和方向计算方向
    if 35<dig<145:
        if 'S' in d:
            y = (y[0], y[1]*-1)
        if y[1] < e[1]:
            dir = 'F'
        else:
            dir = 'B'
    else:
        if 'S' in d:
            dig = abs(dig-180)
            pass
        if 0<=dig<=35:
            dir = 'R'
        else:
            dir = 'L'
    
    return [dir, dist]

#转换为X，Y坐标的函数
def genPos(p):
    x = (ord(p[0])-65)
    y = int(p[1])*-1
    if x & 1:
        y -= 0.5
    else:
        y += 0.5
    return [x, y]
    
#求向量的角的函数
def culcDegrees(posA, posB, posC):
    vecA = [x - y for (x, y) in zip(posA, posB)]
    vecB = [x - y for (x, y) in zip(posC, posB)]
    cos = (vecA[0]*vecB[0]+vecA[1]*vecB[1])/(math.sqrt(vecA[0]**2+vecA[1]**2)*math.sqrt(vecB[0]**2+vecB[1]**2))
    return round(math.degrees(math.acos(cos)),1)


if __name__ == '__main__':
    assert find_enemy('G5', 'N', 'G4') == ['F', 1], "N-1"
    assert find_enemy('G5', 'N', 'I4') == ['R', 2], "NE-2"
    assert find_enemy('G5', 'N', 'J6') == ['R', 3], "SE-3"
    assert find_enemy('G5', 'N', 'G9') == ['B', 4], "S-4"
    assert find_enemy('G5', 'N', 'B7') == ['L', 5], "SW-5"
    assert find_enemy('G5', 'N', 'A2') == ['L', 6], "NW-6"
    assert find_enemy('G3', 'NE', 'C5') == ['B', 4], "[watch your six!]"
    assert find_enemy('H3', 'SW', 'E2') == ['R', 3], "right"
    assert find_enemy('A4', 'S', 'M4') == ['L', 12], "true left"
    print("You are good to go!")
