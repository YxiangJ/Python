
def steps_to_convert(line1, line2):
    if line1 == line2 == '':
        return 0  # ('', '') -> nothing to do
    if line1 == '':
        return len(line2)  # ('', 'line') -> ('line', 'line') ... append 'line'
    if line2 == '':
        return len(line1)  # ('line', '') -> ('', '') ... remove 'line'

    # When first characters are same, skip it ('line', 'line') -> ('ine', 'ine')
    if line1[0] == line2[0]:
        return steps_to_convert(line1[1:], line2[1:])

    # Delete ('aline', 'line') -> ('line', 'line') ... remove 'a'
    n1 = steps_to_convert(line1[1:], line2)
    # Insert ('ine', 'line') -> ('line', 'line') ... prepend 'l'
    n2 = steps_to_convert(line2[0] + line1, line2)
    # Replace ('xine', 'line') -> ('line', 'line') ... replace 'x' with 'l'
    n3 = steps_to_convert(line2[0] + line1[1:], line2)

    return min(n1, n2, n3) + 1


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert steps_to_convert('line1', 'line1') == 0, "eq"
    assert steps_to_convert('line1', 'line2') == 1, "2"
    assert steps_to_convert('line', 'line2') == 1, "none to 2"
    assert steps_to_convert('ine', 'line2') == 2, "need two more"
    assert steps_to_convert('line1', '1enil') == 4, "everything is opposite"
    assert steps_to_convert('', '') == 0, "two empty"
    assert steps_to_convert('l', '') == 1, "one side"
    assert steps_to_convert('', 'l') == 1, "another side"
    print("You are good to go!")
