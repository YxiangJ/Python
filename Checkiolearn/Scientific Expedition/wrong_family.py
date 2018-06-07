
def is_family(tree):
    fathers = [i[0] for i in tree]
    sons = [i[1] for i in tree]
    if len(sons) > len(set(sons)):
        return False
    if len(set(fathers) - set(sons)) != 1:
        return False
    family = {i[1]: i[0] for i in tree}
    for key, value in family.items():
        if key == value:
            return False
        if value in family.keys():
            if family[value] == key:
                return False
    return True
'''
def is_family(relationships):
    
    fathers = set()
    sons = set()
    
    for f, s in relationships:
        
        #Father's father case
        if [s, f] in relationships:             
            return False

        fathers.add(f)
        sons.add(s)

    #Duplicates sons case
    if len(relationships) > len(sons):
        return False
        
    #the second father and the following must also be part of the sons
    if len(fathers & sons) != len(fathers) - 1:
        return False
         
    return True
'''

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
        ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
    assert is_family([
        ['Logan', 'William'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")
