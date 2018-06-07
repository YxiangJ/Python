#words中的word在text文本中出现的次数统计

def popular_words(text, words):
    # your code here
    return dict(zip(words, [text.lower().count(i.lower()) for i in words]))
    '''result = {}
                for word in words:
                    result[word] = text.lower().count(word.lower())
                return result'''


'''
import re
text = re.split('[. , \n]',text.lower())
result_dict = {}
for word in words:
    d = result_dict[word] = text.count(word)
    
return result_dict
'''


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
