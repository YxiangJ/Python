def checkio(data):
    if len(data):
        return data.pop() + checkio(data)
    else:
        return 0
