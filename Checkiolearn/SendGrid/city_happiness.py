def most_crucial(net, users):
    l = []  # list of nodes
    d = {}  # dict containing nodes and their occurrence in connection
    for connection in net:
        for node in connection:
            l.append(node)
    for item in l:
        if item in d.keys():
            d[item] = d[item] + 1
        else:
            d[item] = 1
    maximum = max(d.values())  # finds the max value
    keys = [x for x, y in d.items() if y == maximum]

    maxx = users[keys[0]]
    most_happy = [keys[0]]
    for item in keys:
        if users[item] > maxx:
            maxx = users[item]
            most_happy[0] = item
        elif users[item] == maxx and item not in most_happy:
            most_happy.append(item)
    return most_happy

'''
import copy
import math

def getnode(nodes,crush):
    mycity = ''
    for node in nodes:
        if node != crush:
            mycity = node

    return mycity
#计算独立的网络
def subnetworks(net, crush):
    subnetlist = []
    netcopy = copy.deepcopy(net)
    #崩溃节点列表
    crushlist = []
    # 将坏的节点扣除
    for net1 in net:
        if crush in net1:
            temp1 = getnode(net1, crush)
            crushlist.append(temp1)
            if net1 in netcopy:
                netcopy.remove(net1)

    # 计算坏的网络
    # 排除空元素干扰
    while '' in crushlist:
        crushlist.remove('')
    #算出独立的点是否包含在网络中
    sidenetwork = []
    netcopy1 = copy.deepcopy(netcopy)
    crushlistcopy = copy.deepcopy(crushlist)

    for net1 in netcopy:
        for crush in crushlist:
            if crush in net1:
                for net2 in net1:
                    if net2 not in sidenetwork:
                        sidenetwork.append(net2)
                #把有边的删除，剩下的就是独立的点
                if crush in crushlistcopy:
                    crushlistcopy.remove(crush)
            else:
                for net2 in net1:
                    if net2 not in sidenetwork:
                        sidenetwork.append(net2)

    for crush in crushlistcopy:
        subnetlist.append(crush)

    subnetlist.append(sidenetwork)
    return subnetlist
#计算影响人数，根据独立的网络计算
def crucialusers(subnetlist,users):

    total = 0
    for subnet in subnetlist:
        num = 0
        for key in subnet:
            num = num + users.get(key)

        total = total + math.pow(num,2)

    return total

def most_crucial(net, users):
    keylist = []

    keys = users.keys()
    crucialdict = {}
    crucialkeylist = []
    crucialvaluelist = []
    citylist = []
    for key in keys:
        keylist.append(key)
    for key in keylist:
        subnetlist = subnetworks(net,key)
        crushusers = crucialusers(subnetlist,users)
        crucialdict[key] = crushusers

    #tempkey = min(zip(crucialdict.values(), crucialdict.keys()))
    for key in crucialdict.keys():
        crucialkeylist.append(key)
    for value in crucialdict.values():
        crucialvaluelist.append(value)
    temp9 = crucialvaluelist[0]
    index9 = 0
    minlist = []
    #先找出最小值
    for index in range(len(crucialvaluelist)):
        if index > 0:
            if crucialvaluelist[index] < temp9:
                temp9 = crucialvaluelist[index]
                index9 = index

    #再找出和最小值相同的值
    #使用排除法，排除0和最小值这两个坐标
    minlist.append(index9)
    for index in range(len(crucialvaluelist)):
        if crucialvaluelist[index] == temp9 and index not in (0,index9):
            minlist.append(index)

    print(minlist)
    for temp in minlist:
        print(crucialkeylist[temp])
        citylist.append(crucialkeylist[temp])
    print(str(crucialdict))
    #print(tempkey)
    #citylist.append(tempkey[1])
    return citylist
'''

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_crucial([
        ['A', 'B'],
        ['B', 'C']
    ], {
        'A': 10,
        'B': 10,
        'C': 10
    }) == ['B'], 'First'

    assert most_crucial([
        ['A', 'B']
    ], {
        'A': 20,
        'B': 10
    }) == ['A'], 'Second'

    assert most_crucial([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E']
    ], {
        'A': 0,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10
    }) == ['A'], 'Third'

    assert most_crucial([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 10,
        'D': 20
    }) == ['B'], 'Forth'

    print('Nobody expected that, but you did it! It is time to share it!')
