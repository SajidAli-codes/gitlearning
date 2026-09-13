class credentails:
    def __init__(self,name,password):
        self.name=name
        self.password=password

student1=credentails("kaka","1234")   


while(True):
    name=input("Username ")
    password=input("Password ")

    if(name==student1.name and password==student1.password):
        print("loginn successfull")
        break
    else:
        print("Invalid password or username")
        continue

