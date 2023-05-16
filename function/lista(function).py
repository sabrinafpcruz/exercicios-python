def listanova(l1):
    l2=[]
    for a in l1:
        if a != l2:
            l2.append(a)
    return l2

def lista2(l1):
    return list(set(l1))

a=[1,2,2,3,4,4,5,3,6,7,6,8]
print(listanova(a))
print(lista2(a))