g="I am {} ,I am {}"
name="Abhay"
st="Multimillionarie"
print(g.format(name,st)) #but the problem in this it give sequencing wise allotment 
print(f"I am {name}, I am {st}")
#if u want to see where the variable is added
print(f"I am {{name}}, I am {{st}}")

price=23.5634
print(f"the price is {price:.2f}")


print(f"{2*30}")  #curly bracket multiply product we get