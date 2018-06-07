#选择字符串中出现最多的字母，并按字母顺序显示第一个

# 普通方法
import re
from collections import Counter


def get_max_value(text):
    text = text.lower()
    result = re.findall('[a-z]', text)
    count = Counter(result)
    count_list = list(count.values())
    max_value = max(count_list)
    max_list = []
    for k, v in count.items():
        if v == max_value:
            max_list.append(k)
    max_list = sorted(max_list)
    return max_list[0]


# 精简方法
from collections import Counter


def checkio(text):
    count = Counter([x for x in text.lower() if x.isalpha()])
    m = max(count.values())
    return sorted([x for (x, y) in count.items() if y == m])[0]


# 最佳方法
import string


def checkio(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)


