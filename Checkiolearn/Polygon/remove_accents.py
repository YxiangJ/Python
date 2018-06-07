# 可能是一个部分用户名验证过程或系统，根据用户的名字和姓氏提出用户名

from unicodedata import normalize, category


def checkio(in_string):
    # normalize splits accented letters in two: letter + accent
    # category(c) 'Mn' contains every accent
    # http://www.fileformat.info/info/unicode/category/Mn/list.htm
    return ''.join(c for c in normalize('NFD', in_string) if category(c) != 'Mn')


    # These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
