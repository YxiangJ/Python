'''
3*3方格中，横竖斜一样的胜利，五子棋类似的一种游戏
'''

def checkio(game_result):
	rows = game_result
	cols = map(''.join, zip(*rows))
	diags = map(''.join, zip(*[(r[i], r[2-i]) for i,r in enumerate(rows)]))
	lines = rows + list(cols) + list(diags)

	return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'
'''
zip函数可将两个数组糅合在一起，eg：name=['Any','Bob'],grade=[80,90],zip(name,grade)=[('Any',80),('Bob',90)]
在函数调用中使用*list/tuple的方式表示将list/tuple分开，作为位置参数传递给对应函数（前提是对应函数支持不定个数的位置参数）, 
如test = ["XXX", "OOO", "..."], zip(*test) = [('X', 'O', '.'), ('X', 'O', '.'), ('X', 'O', '.')]
'''

from functools import reduce

def checkio(game_result):
	check_result = game_result

	for i in range(3):
		s = reduce(lambda x,y :x+y, (game_result[j][i] for j in range(3)))
		check_result.append(s)

	s = reduce(lambda x,y:x+y, (game_result[i][i] for i in range(3)))
	check_result.append(s)

	s = reduce(lambda x,y:x+y, (game_result[i][2-i] for i in range(3)))
	check_result.append(s)

	if 'XXX' in check_result:
		return 'X'
	elif 'OOO' in check_result:
		return 'O'
	else:
		return 'D'



def checkio(game_result):
    x = game_result
    cols = [x[0][i] + x[1][i] + x[2][i] for i in range(3)]
    diags = [x[0][0] + x[1][1] + x[2][2], x[2][0] + x[1][1] + x[0][2]]
    x = x + cols + diags
    flag = [y.count('X') == 3 or y.count('O') == 3 for y in x]
    if any(flag):
        return x[flag.index(True)][0]
    else:
        return 'D'