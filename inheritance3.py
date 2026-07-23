class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)
class doctor(person):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept = dept
    def doctor_info(self):
        print("Department:", self.dept)
class patient(person):
    def __init__(self,name,age,illness):
        super().__init__(name,age)
        self.illness = illness
    def patient_info(self):
        print("illness:", self.illness)
class medical_intent(doctor,patient):
    def __init__(self,intent_id):
        self.id = intent_id
    def medical_intent_info(self):
        print("intent ID:", self.id) 
person("ofiq",20).display_person()
doctor("rasool",20,"pharmacy").doctor_info() 
patient("afrid",20,"fever").patient_info() 
medical_intent("ab20045").medical_intent_info() 