class Employee:
    language = "Python"  # This is a class attribute
    salary = 500000  # This is a class attribute
    
    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")
        
    @staticmethod
    def greet():
        print("Hello, welcome to the Employee class!")
        
nirdesh = Employee()

# nirdesh.language ="JavaScript"  # This is an instance attribute
nirdesh.greet() # This will call the static method greet
nirdesh.getInfo()  # This will print the language and salary
# Employee.getInfo(nirdesh)  # This will also work, calling the method on the class with an instance