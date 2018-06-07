# 截图特定范围内的字符串


def between_markers(text, begin, end):
    initial = text.find(begin)
    if initial != -1:
        initial += len(begin)
    else:
        initial = 0

    final = text.find(end)
    if final == -1:
        final = len(text)

    if initial > final:
        return ''
    else:
        return text[initial:final]


"""
import re

def between_markers(text: str, begin: str, end: str) -> str:
    if re.search(f"{re.escape(end)}.*{re.escape(begin)}", text):
        return ""
    return text.split(begin)[-1].split(end)[0]
"""

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers(
        'No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
