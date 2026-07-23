a =int(input("enter 1st num : "))
b =int(input("enter 2nd num : "))
c =int(input("enter 3rd num : "))
if a>b and a>c:
    print("largest number : ",a)
elif b>a and b>c:
    print("largest number : ",b)
else:
    print("largest number : ",c)