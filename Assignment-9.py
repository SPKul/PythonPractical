#python program find cube

def deco(fun):
     def inside ():
          value = fun()
          return value **3
     return inside

@deco
def num():
     return 5
print("Cube of 5 ",num())


       
