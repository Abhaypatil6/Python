# #Reading a file
# f = open('Abhay.txt','r')
# text=f.read()
# print(text)
# f.close()

#Writing a file
f=open('Abhay2','a')
f.write('Abhay is filled with energy')
# print(f)
f.close()

with open('Abhay','a') as f:
    f.write('hello')

    