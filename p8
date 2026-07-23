n = list(input("enter a list of numbers: "))
print(n)
a = []
for i in range(len(n)):
    if n[i] not in a:
        a.append(n[i])
print(a)
for i in range(len(a)):
    if a[i] in n:
        print(f"{a[i]} is repeated {n.count(a[i])} times")