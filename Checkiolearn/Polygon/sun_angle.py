def sun_angle(time):
    # replace this for solution
    l = time.split(':')
    result = (int(l[0]) - 6) * 15 + int(l[1]) / 4
    if int(l[0]) > 18 or int(l[0]) < 6:
        return "I don't see the sun!"
    else:
        return result


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
