class Employee:
    company = "ITC"
    name = "Defualt name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")
        
# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the company is {self.company}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

class Programmer(Employee):
    company = "ITC Infotech"
    language = "Python"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company,b.company)
b.show()
b.showLanguage()