# 在这个任务中，我们使用逻辑二进制操作，这是计算机科学的基础。也许你可以在密码学中找到这个主题的用法？


def checkio(first, second):
    result = 0
    for operator in ('&', '|', '^'):
        res_row = 0
        for i in bin(first)[2:]:
            row = ''
            for j in bin(second)[2:]:
                row += eval('str(int(i) {} int(j))'.format(operator))
            res_row += int(row, 2)
        result += res_row
    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
