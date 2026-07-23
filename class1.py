class bankaccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def show(self):
        print(f"{self.name}'s balance is {self.balance}")
s1 = bankaccount("rasool",2.50)
s2 = bankaccount("ofiq",2.0)
s3 = bankaccount("afrid",-5.34)
s4 = bankaccount("yashwanth",-200)
s1.show()
s2.show()
s3.show()
s4.show()