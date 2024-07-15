def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("The average is: ", sum/len(numbers))
average(5,6)

#     return sum/len(numbers)         # when return is written we have written c and the value of return is stored 
#                                     #  in c then print c .
# c= average(5,6,7,1)
# print(c)