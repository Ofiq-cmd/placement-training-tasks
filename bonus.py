salary = int(input("Enter your salary: "))
service_years = int(input("Enter your years of service: "))

if service_years <5:
    bonus = salary*0.05
elif service_years >=5 and service_years <10:
    bonus = salary*0.10
else:
    bonus = salary*0.20
print("bonus: ",bonus)