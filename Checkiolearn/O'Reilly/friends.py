# 在这里您将实现一个具有可变状态的类。这不是一个简单的结构，有两个函数，但对象表示的结构更复杂。
class Friends:
    def __init__(self, connections):
        self.connections = set(map(frozenset, connections))
        #raise NotImplementedError

    def add(self, connection):
        if frozenset(connection) in self.connections:
            return False
        else:
            self.connections.add(frozenset(connection))
            return True
        #raise NotImplementedError

    def remove(self, connection):
        if connection not in self.connections:
            return False
        else:
            self.connections.remove(connection)
            return True
        #raise NotImplementedError

    def names(self):
        return set().union(*self.connections)
        #raise NotImplementedError

    def connected(self, name):
        return set(n for n in self.names() if {n, name} in self.connections)
        #raise NotImplementedError


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
    print("well done!")
