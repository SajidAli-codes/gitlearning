class user:
    def __init__(self,name,age,gender,phone,gpa):
        self.name=name
        self.age=age
        self.gender=gender
        self.phone=phone
        self.gpa=gpa
    @property
    def userdetails(self):
        return (self.name,self.age,self.gender,self.phone,self.gpa)
    @userdetails.setter
    def userdetails(self,name,age,gender,phone,gpa):
        self.name=name
        self.age=age
        self.gender=gender
        self.phone=phone
        self.gpa=gpa
def adduser():
    name=input("Enter name")
    age=int(input("Enter age"))
    gender=input("Enter male(M) or female(F)")
    phone=int(input("Enter phone number"))
    gpa=float(input("Enter gpa"))
    user1=user(name,age,gender,phone,gpa)
    return user1
user1=adduser()