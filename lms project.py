class lms:
    name=""
    rollnumber=""
    email=""
    password=""
    d={'1': ['a', 'dsf@gmail.com', 'abc']}
    def register(self):
        self.name=input("enter your name:")
        if self.name not in self.d:
            self.rollnumber=input("enter your roll number:")
            self.email=input("enter your email:")
            self.password=input("enter your password:")
            print("succesfully registered")
            self.d[ self.rollnumber]=[self.name, self.email, self.password]
            print(self.d)
        else:
            print("username already exit")
            
    def login(self):
        self.rollonumber=input("enter your rollnumber")
        if self.rollnumber in d:
            self.password=input("enter your password")
            if self.password==self.d[self.rollnumber][-1]:
                print("succesfully register")
            else:
                print("wrong password")
        else:
            print("username does not exist")
            
    def display(self):
        self.r=input("enter rollnumber")
        if self.r in self.d:
            print("Name:",self.d[self.r][0],"\nRollNumber:",self.r,"\nEMail:",self.d[self.r][1])
        else:
            print("user does not exist")

    def logout(self):
        exit
                
c=lms()
print("1.Register \n2.Login\n3.Display\n4.Logout")
i=int(input("enter choice"))
while i:
    if i==1:
        c.register()
    elif i==2:
        c.login()
    elif i==3:
        c.display()
    elif i==4:
        c.logout()
    else:
        print("enter correct option")
    i=int(input("enter 1 or 2"))

        
