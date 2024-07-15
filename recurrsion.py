#Factorial
def Factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*Factorial(n-1)
print(Factorial(5))
print(Factorial(6))
print(Factorial(3))


