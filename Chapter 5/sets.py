e = set() # Don't use s = {} as it is mutable and empty dictonary 

s = {1,2,3,4,5,6,2,3,1}

print(s) # {1, 2, 3, 4, 5, 6}
print(type(s)) # <class 'set'>
print(len(s)) # 6, length of set