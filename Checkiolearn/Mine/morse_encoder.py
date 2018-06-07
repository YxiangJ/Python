MORSE = {'a': '.-', 'b': '-...', 'c': '-.-.',
         'd': '-..', 'e': '.', 'f': '..-.',
         'g': '--.', 'h': '....', 'i': '..',
         'j': '.---', 'k': '-.-', 'l': '.-..',
         'm': '--', 'n': '-.', 'o': '---',
         'p': '.--.', 'q': '--.-', 'r': '.-.',
         's': '...', 't': '-', 'u': '..-',
         'v': '...-', 'w': '.--', 'x': '-..-',
         'y': '-.--', 'z': '--..', '0': '-----',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.'
         }


def morse_encoder(text):
    # replace this for solution
    text = text.lower()
    result = []
    s = ""
    for x in text:
        if x in MORSE.keys():
            result.append(MORSE[x])
        if x == " ":
            result.append(" ")
    s = s + result[0]
    for j in result[1:]:
        s = s + " " + j
    return s


if __name__ == '__main__':
    print("Example:")
    print(morse_encoder('some text'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_encoder("some text") == "... --- -- .   - . -..- -"
    assert morse_encoder("2018") == "..--- ----- .---- ---.."
    assert morse_encoder(
        "It was a good day") == ".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"
    print("Coding complete? Click 'Check' to earn cool rewards!")
