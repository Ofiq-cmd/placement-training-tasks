n =int(input("enter no.of items : "))
price = [0] * n
for i in range(n):
    price[i] = int(input("enter price of item : "))
total = sum(price)
print("total bill : ",total)