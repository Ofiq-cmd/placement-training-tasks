class employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Basic Salary:", self.salary)
    def bonus(self):
        if self.salary >= 50000:
            bonus_amount = self.salary * 0.10
        else:
            bonus_amount = self.salary * 0.05
        print("Bonus Amount:", bonus_amount)
        print()
e1 = employee(101, "ofiq", 60000)
e2 = employee(102, "rasool", 45000)
e3 = employee(103, "sravzz", 70000)
e4 = employee(104, "lilly", 30000)
e5 = employee(105, "sonu", 50000)
employees = [e1, e2, e3, e4, e5]
for emp in employees:
    emp.display()
    emp.bonus()