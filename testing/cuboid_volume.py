'''def cuboid_volume(l):
    if type(l) not in [int, float]:
        raise TypeError('the length of cuboid can only be a valid integer or a float')
    return l*l*l'''

pewe = []
size = 0
def add(value):
    if value in pewe:
        return False
    else:
        pewe.append(value)
        return True
def size():
    return len(pewe)
def checkElements(value):
    check = [i for i in pewe if i == value]
    return check
def delete (value):
    pewe.remove(value)
    return True

