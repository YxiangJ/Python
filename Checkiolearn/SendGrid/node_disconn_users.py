#一个网络中接不到信息的用户数

def disconnected_users(net, users, source, crushes):
    crushes = set(crushes)
    if source in crushes:
        return sum(users.values())

    visited = set()
    stack = {source}
    while stack:
        current = stack.pop()
        visited = visited | {current}
        for left, right in net:
            if right == current:
                if left not in visited and left not in crushes:
                    stack = stack | {left}
            elif left == current and (right not in visited and right not in crushes):
                stack = stack | {right}
    return sum(v for k, v in users.items() if k not in visited)

'''def disconnected_users(net, users, source, crushes):
    connected = {source}
    if source in crushes: connected = set()
    while True:
        for link in net:
            if len(set(link) & connected) == 1 and \
               len(set(link) & set(crushes)) == 0:
                connected = connected | set(link)
                break
        else: break
    return sum([users[node] for node in set(users.keys()) - connected])'''

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"

    print('Done. Try to check now. There are a lot of other tests')
