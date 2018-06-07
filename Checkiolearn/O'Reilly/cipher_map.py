'''
在这里您可以学习如何使用2d数组。
您还可以了解古代的格栅的密码，一个编码的消息已经过去半个世纪的技术。
已知的最早描述格栅密码来自意大利数学家卡丹诺卡尔达诺1550。
'''


def recall_password(cipher_grille, ciphered_password):
    solution = []
    for _ in range(4):
        for rows in zip(cipher_grille, ciphered_password):
            for g, p in zip(*rows):
                if g == 'X':
                    solution.append(p)
        cipher_grille = list(zip(*cipher_grille[::-1]))
    return ''.join(solution)


def recall_password(grille, pw):
    solution = []
    for _ in range(4):
        for rows in zip(grille, pw):
            for g, p in zip(*rows):
                if g == 'X':
                    solution.append(p)
        grille = list(zip(*grille[::-1]))
    return ''.join(solution)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
    print("well done!")
