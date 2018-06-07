#设置的密码中包含大小写字母及数字

def checkio(data):
    if (len(data) >= 10 and any(x.isupper() for x in data)
        and any(x.islower() for x in data)
            and any(x.isdigit() for x in data)):
        return True
    else:
        return False

    # replace this for solution
    return True or False

# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


def checkio(data):
    if(len(data) >= 10 and any(x.isupper() for x in data)
            and any(x.islower() for x in data)
            and any(x.isdigit() for x in data)):
        return True
    else:
        return False
