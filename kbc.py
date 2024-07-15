print('Print Yes to start: ')
Type_here=input()
for i in range(3):
     if(Type_here=='yes'):
          print("\n1. Among which animal , the sound of animal is called ''/bark/'' : \nA.Cat \nB.Dog\nC.camel\nD.parrot " )
          Answer=input()
          if(Answer=='b'):
               print("Sahi jawab")
          else:
               print('GALAT JAWAB')
          print("\n2. what is the colour of the sky: \nA.blue\nB.Green\nC.yellow\nD.white")
          Answer=input()
          if(Answer=='a'):
               print("Sahi jawab")
          else:
               print("GALAT JAWAB")
     else:
          print("Not valid ")