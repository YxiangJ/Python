# 此任务显示位置密码的差异。有了这个密码，你可以在一本书中隐藏一条消息，让你和接收者发送这些编码消息


def checkio(text, word):
    word = word.lower()
    l1 = text.lower().replace(' ', '').split('\n')
    mx = max([len(l) for l in l1])
    l1 = ["".join([l, " " * (mx - len(l))]) for l in l1]
    l2 = ["".join(x) for x in zip(*l1)]
    f1 = [[x + 1, l.find(word) + 1, x + 1, l.find(word) + len(word)]
          for x, l in enumerate(l1) if word in l]
    f2 = [[l.find(word) + 1, x + 1, l.find(word) + len(word), x + 1]
          for x, l in enumerate(l2) if word in l]
    return f1[0] if len(f1) > 0 else f2[0] if len(f2) > 0 else []


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
