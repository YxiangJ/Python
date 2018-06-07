import copy
"""
*算法思想：
*1，将崩溃的节点从网络中删除（这里使用了深复制，python删除时会有一点小问题）。
*2，得到和崩溃相连的节点，并添加为列表A。
*3，计算列表A的长度，即有多少个节点，认为有多少个独立网络，这个需要下一步进行调整。
*4，将列表A的节点和网络剩下的边进行匹配，如果边存在于崩溃列表中，说明列表A中点是相连的，要把网络减一
*
"""


def getnode(nodes, crushes):
    mycity = ''
    for node in nodes:
        if node not in crushes:
            mycity = node

    return mycity


def subnetworks(net, crushes):
    netcopy = copy.deepcopy(net)
    crushlist = []
    # 将坏的节点扣除
    for net1 in net:
        for crush in crushes:
            if crush in net1:
                temp1 = getnode(net1, crushes)
                crushlist.append(temp1)
                if net1 in netcopy:
                    netcopy.remove(net1)

    # 计算坏的网络
    # 排除空元素干扰
    while '' in crushlist:
        crushlist.remove('')
    side1 = len(crushlist)

    # 列表中有两个点相连的，要减一
    # 或者有单独的点在边里，也删除，直到剩下孤立的边和点
    for net1 in netcopy:
        if net1[0] in crushlist and net1[1] in crushlist:
            side1 = side1 - 1

    return side1


'''def subnetworks(net, crushes):
    nodes = set(sum(net, [])) - set(crushes)
    subcount = 0
    while nodes:
        subcount += 1
        stack = [nodes.pop()]
        while stack:
            node = stack.pop()
            for conn in net:
                if node == conn[0] and conn[1] in nodes:
                    stack.append(conn[1])
                    nodes.remove(conn[1])
                if node == conn[1] and conn[0] in nodes:
                    stack.append(conn[0])
                    nodes.remove(conn[0])
    return subcount'''


'''def subnetworks(net, crushes):
    in_order = [''.join(pair) for pair in net if pair[0] not in crushes and pair[-1] not in crushes]
    in_order = '-'.join(in_order)
    
    net = '-'.join(list(map(''.join, net)))
    for x in crushes: net = ''.join(net.split(x))
    net = [x for x in net.split('-') if len(x) is 1 and x not in in_order or len(x) is 2]
    return len(net)'''

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['B']) == 2, "First"
    assert subnetworks([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['D', 'F']
    ], ['A']) == 3, "Second"
    assert subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')
