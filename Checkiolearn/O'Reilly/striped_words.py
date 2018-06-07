VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

'''这个任务中的这个想法对语言研究和分析是一个有用的练习。
文本处理是分析各种书籍和语言的主要工具之一，可以帮助将印刷文本转换成数字格式。'''


def checkio(text):

    txt = ''.join(c.upper() if c.isalnum() else ' ' for c in text).split()
    total = 0
    for word in txt:
        if len(word) < 2:
            continue
        odd = set(word[1::2])
        even = set(word[::2])
        total += ((odd <= set(VOWELS) and even <= set(CONSONANTS)) or
                  (odd <= set(CONSONANTS) and even <= set(VOWELS)))
    return total


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    print("well done!")
