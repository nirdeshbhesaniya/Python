class Employee:
    language = "Python"  # This is a class attribute
    salary = 500000;
    
    
nirdesh = Employee()
nirdesh.language = "JavaScript" # This is an instance attribute
print(nirdesh.language, nirdesh.salary)



# Here name is instance attribute and salary and language are class attributes as they directly belong to the class