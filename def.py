def factorial(n) :
    a = 1
    for i in range (1, n+1) :
        a *= i

    return a

x = int(input())
x = factorial(x)
print (x)
