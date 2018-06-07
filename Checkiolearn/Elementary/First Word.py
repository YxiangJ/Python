#提取一段文本中的首歌单词


'''def first_word(text: str)->str:
    """
    returns the first word in a given text
    """
    # your code here
    import re
    result = re.search("[a-zA-Z']+", text)
    text = str(result.group())
    return text'''

'''import re
def first_word(text: str)->str:
    for word in re.sub('[.,]', '', text).split(' '):
        if len(word) == 0:
            pass
        else:
            return word
    return 0'''
import re


def first_word(text: str)->str:
    return re.search("[a-zA-Z']+", text)[0]


'''def first_word(text: str) -> str:
    text = text.replace(',', '')
    text = text.replace('.', ' ')
    li = text.split()
    char = li[0]
    """
        returns the first word in a given text.
    """
    # your code here
    return char'''


if __name__ == '__main__':
    print("Examples:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert first_word("Hello world") == "Hello"
    #assert first_word(" a word ") == "a"
    #assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")
