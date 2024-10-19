class Employee:
    company="Google"
    def getSalary(self):
     print(f"salary for this employee working in {self.company} is {self.salary} ")
    @staticmethod
    def greet():
        print("Good Morning ,Sir!")

rohit=Employee()    
rohit.salary=20000
rohit.getSalary()
rohit.greet() 

# Employee.getSalary(rohit)
