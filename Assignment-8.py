#WAP to store student roll number and marks using dictionary. 
d= {1: 56 , 4: 47 , 5: 88 , 2: 99 }
print("Student Info = ",d)
def add_element():
     k = int (input("Enter roll number of student = "))
     v = int (input("Enter Marks of student = "))
     d.update({k:v})
     print("After add",d)
def delete():
      num = int(input("Enter roll no for delete student info = "))
      d.pop(num)
      print("After Delete",d)
      print("Record Deleted Sussfully!!")
def update():
       num = int(input("Enter total number of Student = "))
       for i in range(num):
        k = int (input("Enter roll number of student = "))
        v = int (input("Enter Marks of student = "))
        d.update({k:v})
        print("After Update",d)
def search():
      r = int(input("Enter roll number to search marks = "))
      marks = d.get(r,-1)
      if(marks != -1):
            print("Roll number ",r,"marks",marks)
      else:
            print("Record not found!!")
def sort_ascending():
      print("Sort by ascending =",sorted(d.items(), key =
             lambda kv:(kv[1], kv[0])))   
def sort_descending():
      print("Sort by descending =",sorted(d.items(), key =
             lambda kv:(kv[1], kv[0]),reverse=True))
def display():
       for k in d:
                 print("Roll No :",k, "Marks :",d[k])
                 
def maeks_max():
       print("Highest marks =",max(d.items(), key =
                          lambda kv:(kv[1], kv[0])))
              
# Ask for the user's choice.
choice = ' '

# Start a loop that runs until the user enters the value for 'quit'.
while choice != '9':
 # Give all the choices in a series of print statements.
  print("\n\n[1] Add record")
  print("[2] Delete record ")
  print("[3] Update Marks ")
  print("[4] Search a roll number and display marks ")
  print("[5] Sort by Ascending  order ")
  print("[6] Sort by Descending order  ")
  print("[7] Display student information .")
  print("[8] highest marks.")
  print("[9] Exit")

  choice = input("\nSelect Option = ") 
  if choice == '1':
         add_element()
  elif choice == '2':
          delete()
  elif choice == '3':
         update()
  elif choice == '4':
         search()
  elif choice == '5':
         sort_ascending()
  elif choice == '6':
         sort_descending()
  elif choice == '7':
         display()
  elif choice == '8':
         maeks_max()
  elif choice == '9':
          exit()
  else:
         print("Option not found ")

















       
