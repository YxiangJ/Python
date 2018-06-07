#显示列表中不唯一的元素
def checkio(data):
    list = []
    for i in data:
        if list.count(i) > 1:
            list.append(i)
    return list
