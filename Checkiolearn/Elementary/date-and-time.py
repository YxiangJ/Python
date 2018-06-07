#时间转换为字符串

from datetime import datetime

def date_time(time):
    d = datetime.strptime(time, "%d.%m.%Y %H:%M")
    h = "hour" if d.hour == 1 else "hours"
    m = "minute" if d.minute == 1 else "minutes"
    return f"{d.day} {d.strftime('%B')} {d.year} year {d.hour} {h} {d.minute} {m}"


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time(
        "01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time(
        "09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time(
        "20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
