# 输出字典中值较大的键


def best_stock(data):
    a = 0.00
    key = ''
    for k, v in data.items():
        if v > a:
            a = v
            key = k
    return key


'''
def best_stock(data):

    return max(data, key=lambda x: data[x])'''



'''def best_stock(data):
    max=0
    for key in data:
        if data[key]>max:
            max=data[key]
            max_stock=key
    return max_stock'''

if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")
