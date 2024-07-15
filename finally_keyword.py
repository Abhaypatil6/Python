def func():
    try:
        l=[2,5,3,7,4,8]
        n=int(input("Enter index:"))
        print(l[n])
        return 1
    except:
        print('invalid output')
        return 0
    finally:
        print("it is always printed")
        
    # print('it is printed')

x=func()
print(x)