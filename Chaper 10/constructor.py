class Employee:
    language = "Python"  # This is a class attribute
    salary = 500000  # This is a class attribute
    def __init__(self, name, salary, language):
        self.name = name  # This is an instance attribute
        self.salary = salary  # This is an instance attribute
        self.language = language  # This is an instance attribute
        print("I am creating an object")
        
    def getInfo(self):
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")
    
    @staticmethod
    def greet():
        print("Hello, welcome to the Employee class!")
        
nirdesh = Employee("Nirdesh", 600000, "JavaScript")
# nirdesh.name = "Nirdesh Bhesaniya"

print(nirdesh.name, nirdesh.language, nirdesh.salary)

rohan = Employee("rohan", 700000, "Java")
        
    
          
        