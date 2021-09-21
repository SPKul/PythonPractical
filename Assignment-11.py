class Employee:
    __id=0
    __name=""
    __designation=""
    __dept=""
    __qualification =""
    __experience=""
    __salary=0
	
    
    def setData(self,id,name,designation,dept,qualification,experience,salary):
        self.__id=id
        self.__name = name
        self.__designation = designation
        self.__dept = dept
        self.__qualification = qualification
        self.__experience = experience
        self.__salary = salary
	

    def showData(self):
        print("Id\t\t:",self.__id)
        print("Name\t\t:", self.__name)
        print("Designation\t:", self.__designation)
        print("Dept\t\t:", self.__dept)
        print("Qualification\t:", self.__qualification)
        print("Experience\t:", self.__experience)
        print("Salary\t:\t", self.__salary)

# main function definition
def main():
    #Employee Object
    emp=Employee()
    emp.setData(1,'Shrawani','Manager','Sales','MBA','Five Years',55000)
    emp.showData()
							
if __name__=="__main__":
    main()

days=float(input("Enter No Days Present:"))
wages=float(input("Enter wages per Day:"))
basic=wages*days;
HRA=basic*0.1;
DA=basic*0.05;
PF=basic*0.12;  
netsalary=basic+HRA+DA-PF;
print("\nBasic:%lf \nHRA:%lf \nDA:%lf \nPF:%lf \nNet Salary:%lf" %(basic,HRA,DA,PF,netsalary));

