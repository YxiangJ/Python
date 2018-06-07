#判断列表中唯一只有一个元素

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    # return len(set(elements)) < 2
    return len(set(elements)) in [0, 1]

#all_the_same = lambda e:e[1:] == e[:-1]
#all_the_same = lambda a:len(set(a)) in {0,1}


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
