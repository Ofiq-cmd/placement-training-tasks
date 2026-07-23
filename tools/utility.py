def is_even(n):
    if n%2==0:
        return "even"
    else:
        return "Odd"
def average(n):
    return sum(n)/len(n)
def check(n):
    for i in len(n):
        return max[i],min[i]
def kg_to_p(n):
    return n/1000
def p_to_kg(n):
    return n*1000
def r_string(n):
    for i in range(len(n),0,-1):
        return i
def counts(n):
    count = 0
    l = ['a','e','i','o','u']
    for i in l:
        if i in n:
            count += 1
    return count
def palindrome(n):
    print("given",n)
    while n>0:
        t=0
        a = n%10
        t += a
        n = n//10
    return t
