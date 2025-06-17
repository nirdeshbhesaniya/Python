class Demo:
    a = 4

o = Demo()

print(o.a)  # Accessing class variable directly from the instance
o.a = 5  # Modifying class variable through the instance
print(o.a)  # Accessing modified class variable through the instance    
print(Demo.a)  # Accessing class variable directly from the class