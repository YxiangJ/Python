# 连续三个单词


def checkio(words):
    '''list = words.split()
                for i in range(len(list) - 1):
                    if list[i].isalpha() and list[i + 1].isalpha() and list[i + 2].isalpha():
                        return True
                return False'''
    for word in words.split():
        try:
            int(word)
            count = 0
        except:
            count += 1
            if count == 3:
                return True
                break
    else:
        return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
