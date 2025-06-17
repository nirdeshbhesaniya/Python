from functools import reduce
l  = [111, 2, 65, 5553, 635, 65, 74, 45,55]

def gratest(a,b):
    if(a>b):
        return a
    return b

print(reduce(gratest,l)) 
