'''
理解内置函数如何在更精确的级别上工作。

需要处理不同数据类型; 另外*args, 表示的是位置参数,
 *kwargs表示的是key参数, args的类型为tuple类型,
 参数为min(3, 2)时, args为(3, 2), 参数为min([3, 2])时, args为([3, 2], );
 '''


'''def min(*args, **kwargs):
    key = kwargs.get('key', None)
    rev = kwargs.get('rev', False)
    return sorted(args if len(args) > 1 else args[0], key=key, reverse=rev)[0]


def max(*args, **kwargs):
    key = kwargs.get('key', None)
    return min(*args, key=key, rev=True)'''


# 分割线
'''def max(*args, key=None):
    max_value = None
    if len(args) == 1:
        args = args[0]

    if key is None:
        for i in args:
            if max_value == None or i > max_value:
                max_value = i
    elif key is not None:
        for i in args:
            if max_value == None or key(i) > key(max_value):
                max_value = i

    return max_value


def min(*args, key=None):
    min_value = None
    if len(args) == 1:
        args = args[0]

    if key is None:
        for i in args:
            if min_value == None or i < min_value:
                min_value = i
    elif key is not None:
        for i in args:
            if min_value == None or key(i) < key(min_value):
                min_value = i

    return min_value'''

# 分割线，在len(arg) == 1的情况, 仍然需要提取出实际的对象, 如([1, 2], )中的[1, 2]; 高明的地方在于使用了sorted, 省去了自己判断类型


def get_first_from_sorted(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key=key, reverse=reverse)[0]


def min(*args, key=None):
    return get_first_from_sorted(args, key, False)


def max(*args, key=None):
    return get_first_from_sorted(args, key, True)


# 分割线
'''def min(*args, **kwargs):
    key = kwargs.get("key", None)
    min_list = []
    if len(args) == 1:
        for arg in args[0]:
            min_list.append(arg)
    elif len(args) > 1:
        for arg in args:
            min_list.append(arg)
    min_list.sort(key=key)
    return min_list[0]


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    max_list = []
    if len(args) == 1:
        for arg in args[0]:
            max_list.append(arg)
    elif len(args) > 1:
        for arg in args:
            max_list.append(arg)
    max_list.sort(key=key, reverse=True)
    return max_list[0]'''


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [
        9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
