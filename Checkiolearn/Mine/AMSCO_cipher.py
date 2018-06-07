# 编码和解码


def decode_amsco(message, key):
    charcnt = len(message)
    message = filter(lambda x: x.isalpha(), message)
    key = str(key)
    keylength = len(key)
    n = charcnt
    grid = []
    rowcnt = 0
    while n > 0:
        row = []
        grid.append(row)
        for i in range(keylength):
            v = min((i + rowcnt) % 2 + 1, n)
            row.append(v)
            n -= v
        rowcnt += 1
    it = iter(message)
    for _, col in sorted(zip(key, range(keylength))):
        for r in range(rowcnt):
            grid[r][col] = ''.join(next(it) for _ in range(grid[r][col]))
    return ''.join(map(''.join, grid))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert decode_amsco("oruoreemdstmioitlpslam",
                        4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco('hrewhoorrowyilmmmoaouletow',
                        123) == "howareyouwillhometommorrow", "How are you"
