lst1 = [1.0,1.0,2.0]
lst2 = [1.2,1.2,2.2]

lst1 = map(sum, zip(lst1, lst2))

myInt = 2
    
#newList[:] = [lst1 / myInt for x in lst1]
newList = map(lambda lst1: lst1/myInt, lst1)

print newList