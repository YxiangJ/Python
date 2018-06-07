def checkio(expression):
    brackets = dict(zip(('(', '[', '{'), (')', ']', '}')))
    for sym in expression:
        if sym.isdigit() or sym in ('+', '-', '*', '=', '/'):
            expression = expression.replace(sym, '')
    if not expression: return True
    list_sym=list(expression)
    while list_sym:
        i=0
        while i<len(list_sym)-1:
            if list_sym[i+1]==brackets.get(list_sym[i]):
                list_sym[i:i+2]=[]
                i=0
                continue
            i+=1
        if list_sym: return False
    else:
        return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"