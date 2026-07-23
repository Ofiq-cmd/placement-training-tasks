class employee:
    def __init__(self,id,name,dept):
        self.id = id
        self.name = name
        self.dept = dept
    def show(self):
        print(f"emp_id : {self.id}")
        print(f"emp_name : {self.name}")
        print(f"emp_dept : {self.dept}")
employees = []
n = int(input("Enter no.of employees to take in :"))
for i in range(n):
    id = input("enter employ id :")
    name = input("enter empolyee name :")
    dept = input("enter department of employee :")
    print("\n")
    s1 = employee(id,name,dept)
    employees.append(s1)
for emp in employees:
    emp.show()