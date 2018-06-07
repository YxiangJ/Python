# 这与孩子们发明他们自己的“鸟”语言时使用的密码相似。现在，您将准备破解代码。
VOWELS = "aeiouy"


def translate(phrase):
    human_phrase = []
    i = 0

    while i < len(phrase):
        human_phrase.append(phrase[i])
        if phrase[i] in VOWELS:
            i += 3
        elif phrase[i] == ' ':
            i += 1
        else:
            i += 2
    return ''.join(human_phrase)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("well done!")
