def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    i = 0
    print(number)
    while abs(number) >= base and len(powers) - 1 > i:
        number = float(number) / float(base)
        i += 1
    if decimals == 0:
        string = str(int(number))
    else:
        if round(number, decimals) - int(number) == 0:
            string = str(int(number)) + "." + "0" * decimals
        else:
            string = str(round(number, decimals))
    string += powers[i] + suffix
    return string


'''    
    from decimal import Decimal
    number = Decimal(number)
    power = 0
    while abs(number) >= base and power < len(powers) - 1:
        power += 1
        number /= base
    number = round(number, decimals) if decimals else int(number)

    return '{:.{dec}f}{}{}'.format(number, powers[power], suffix, dec=decimals)

    return (number)
'''


if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024,
                           suffix='iB') == '976MiB', '976MiB'
