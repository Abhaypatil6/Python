a=input('Enter :')
print(f"The multiplication of table {a} is")
try:
    for i in range(1,11):
        print(f"{a}x{i}={int(a)*i}")        #when string is passed,error is handle
        
except:
    print('invalid input')

print('Abhay is billionarie')
