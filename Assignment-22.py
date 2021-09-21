from collections import Counter

intTuple = ()
#Create Tuple
# Add an Item to Tuple
intTuple = (10, 20, 30, 40, 50)
number = int(input("Enter the Total Number of Tuple Element = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Tuple value = " %i))
    intTuple = intTuple + (value,)
   
print("New Adding Element= ", intTuple)

#Update Element
Uptuple= list(intTuple)
Uptuple[1] = 100
intTuple= tuple(Uptuple)
print("Updateing 1th Element",intTuple)

#Delete Element
intTuple = intTuple[:3] + intTuple[4:]
print("After Removing 4yh Element = ", intTuple)

#Reverse Element
def Reverse(intTuple):
    new_tup = intTuple[::-1]
    return new_tup

print("After Reverse Element",Reverse(intTuple))

#Repeated Element
for k, v in Counter(intTuple).items():
    if v > 1:
        print("Repeated: {}".format(k))












