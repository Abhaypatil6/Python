def square(n):
    ''' Takes the input and square it'''
    print(n**2)
print("Enter value")
s=int(input())
square(s)
print(square.__doc__)  # doc string is used after function define or before body