class Employee:
    language = "Python"
    salary = 500000;
    
    
harry = Employee()
harry.name = "Nirdesh"

print(harry.name, harry.language, harry.salary) 

rohan = Employee()
rohan.name = "Rohan"

print(rohan.name, rohan.language, rohan.salary)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class