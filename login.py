class credentails:
    def __init__(self,name,password):
        self.name=name
        self.password=password

    @property
    def credentials(self):
        return (self.name, self.password)

    @credentials.setter
    def credentials(self, name,password):
        self.name=name
        self.password = password

    def authenticate(self,name,passwrod):
        if (self.name==name and self.password== passwrod):
            return True
        else:
            return False
    

def UpdatePassword():
    new_password=input("Enter the new password:");
    new_username=input("enter the new username:");
    if student1.authenticate(new_username,new_password)==True:
        print("Password updated successfully");
        student1.credentiasl(new_username,new_password);

student1=credentails("kaka","1234")   


while(True):
    print("Enter the username and the password to login")
    name=input("Username ")
    password=input("Password ")
    print("Enter the 1 to update the password any key to continue")
    choice=input()
    if choice=="1":
        UpdatePassword()

    if(name==student1.name and password==student1.password):
        print("loginn successfull")
        break
    else:
        print("Invalid password or username")
        continue
