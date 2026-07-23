n = int(input("enter balance :"))
draw = int(input("enter draw amount :"))
if draw <n:
    print("withdrawal successful")
    a= n-draw
    print("balance is ",a)
else:
    print("insufficient")