class Employee:
    company="Google"
    def _init_(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
         
        print("Emplotee is created")
    def getDetails(self)    :
        print("The name of the employee is ")
    def getSalary(self,name,salary,subunit):
     print(f"salary for this employee working in {self.company} is {self.salary} ")
    @staticmethod
    def greet():
        print("Good Morning ,Sir!")
rohit=Employee("Rohit",100,"Youtube") 
