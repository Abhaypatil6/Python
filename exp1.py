#strings 
name="Abhay"
print("my name is ",name)

#List
m_list=[2,5,'a',7,'b']
print("List is ",m_list)

#Array
m_array=[1,3,4,6,7]
fst_elem=m_array[0]
m_array[2]=5
m_array.append(9)
length=len(m_array)
print("Array is",m_array)
print("first element :",fst_elem)
print("Length of array:",m_array)

#Dictionary
m_dict={"name":"Abhay","Age":"20","City":"Kalyan"}
person_name=m_dict['name']
print("Dictionary is:",m_dict)
print("Person name:",person_name)

#Sets
m_set={2,4,5,7,8}
m_set.add(6)
m_set.remove(4)
print("Set is:",m_set)

#Tuple
m_tuple=(2,4,6,7,8)
first_element=m_tuple[3]
a,b,*rest=m_tuple
print("Tuple:",m_tuple)
print("First element:",first_element)

# conditional statement
# If-else statement
n=6
if(n%2==0):
    print('even')
else:
    print('odd')

#For loop
colors = ['red','orange','yellow','black']
for color in colors:
     print("Loop of color is",color)

#While loop
count=8
while(count>0):
     print("count:",count)
     count=count-1
else:
     print('done ')