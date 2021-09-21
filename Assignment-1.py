#Pyramid
for i in range(1,11):
          print('*  ' *(i))

#Reverse Pyramid
n=40
for i in range (11,0,-1):
     print('  ' *n,end= '  ')
     print(' * '*(i))
     n= n+1

# Left Pyramid
n=40
for i in range(1,11):
          print(' ' *n,end= '  ')
          print(' *' *(i))
          n= n-3
