amount =int(input("enter amount : "))
discount = 0
if amount <5000:
    discount = amount*0
elif amount >=5000 and amount <10000:
    discount = amount*0.10
else:
    discount = amount*0.20
print("discount : ",discount)
final = amount-discount
print("final amount : ",final)