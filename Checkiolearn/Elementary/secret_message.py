def find_message(text):
    """Find a secret message"""
    result = ""
    for ch in text:
        if ch.isupper():
            result += ch
    return result

    # return ''.join([x for x in text if x.isupper()])


'''
import re
def find_message(text):
    return ''.join(re.findall(r"[A-Z]+", text))
'''


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message(
        "How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
