#wap to display even and odd count in a list

ls = list(range(1,24))
print("List is ",ls)
even = odd=0
for i in ls:
      if(i %2 ==0):
          even = even +1
      else:
              odd = odd+1

print("Even count ", even)
print("odd count ", odd)
