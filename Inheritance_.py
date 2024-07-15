class abhay:
    def __init__(self,name,id) :
        self.name=name
        self.id=id
    def details(self):
        print(f"The employee {self.id} name is {self.name}")

class programmer(abhay):
    def lang(self):
        print('Language is great')
l=['ramesh','suresh','rajesh','harsh','sonali','mangesh','nilesh','rahul','raj','parth']
n=0
for i in l:
    n+=10
    a=programmer('ram',4)
    a.details()
    a.lang()