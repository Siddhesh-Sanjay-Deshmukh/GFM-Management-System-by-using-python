l=["Abhi"]
l1=["1234"]
l2=["Chris"]
l3=["123"]
l5=["Regarding New ID Cards"]
l6=["It is my Request to Please Provide us with new ID cards ASAP"]
l7=["Abhi"]
l8=["Regrading Holidays"]
l9=["For how much Time Period We will be given Holidays"]
l4=["Abhi"]
l10=[]


def Display():
    for i in range(0,len(l)):
        print(i,".","Name:",l[i],"Attendance Percentage:",l10[i])
        print("\t")
        
def P():
    for i in range(0,len(l)):
        print("Enter Attendance Percentage for",l[i])
        print("\t")
        x=input("Enter:")
        print("\t")
        l10.append(x)
        print("\t")
    
def help_T():
    print("Select By Name whose Request would you like to Access:")
    print("\t")
    for i in range(0,len(l5)):
        print(l5[i])
        print("\t")
    
    j=input("Enter The Name:")
    print("\t")
    for i in range(0,len(l4)):
        if(j==l5[i]):
            print(l4[i])
            print("\t")
            print(l5[i])
            print("\t")
            print(l6[i])
            print("\t")
        else:
            print("Please enter a Valid Name")
            print("\t")



def doubt_T():
    print("Select By Name whose Request would you like to Access")
    print("\t")
    for i in range(0,len(l7)):
        print(l7[i])
        print("\t")
    
    j=input("Enter The Name:")
    print("\t")
    for i in range(0,len(l7)):
        if(j==l7[i]):
            print(l7[i])
            print("\t")
            print(l8[i])
            print("\t")
            print(l9[i])
            print("\t")    
        else:
            print("Please enter a Valid Name")
            print("\t")




def update_T():
    e=input("Enter Which Personal Information would You Like to Update?:")
    print("\t")
    if(e=="N" or e=="n"):
        f=input("Enter The New Name:")
        print("\t")
        for i in range(0,len(l)):
            if(l[i]==c):
                l[i]=c
                print("Record Updated Successfully..")
                print("\t")
                
    elif(e=="P" or e=="p"):
        f=input("Enter The New Name:")
        print("\t")
        for i in range(0,len(l)):
            if(l1[i]==c):
                l1[i]=c
                print("Record Updated Successfully..")
                print("\t")
    else:
        print("Sorry Enter Valid Option..")



        
    

def Help():
    g=input("Enter The Name:")
    print("\t")
    l4.append(g)
    e=input("Enter The Subject:")
    print("\t")
    l5.append(e)
    f=input("Enter The Describtion:")
    print("\t")
    l6.append(f)
    print("Your Request has been Successfully Recorded And You will be Called by Your GFM Soon...")
    print("\t")

def update():
    e=input("Enter Which Personal Information would You Like to Update?:")
    print("\t")
    if(e=="N" or e=="n"):
        f=input("Enter The New Name:")
        print("\t")
        for i in range(0,len(l)):
            if(l[i]==c):
                l[i]=c
                print("Record Updated Successfully..")
                print("\t")
    if(e=="P" or e=="p"):
        f=input("Enter The New Name:")
        print("\t")
        for i in range(0,len(l)):
            if(l1[i]==c):
                l1[i]=c
                print("Record Updated Successfull")
                print("\t")
    else:
        print("Sorry Enter Valid Option..")
        print("\t")

        

 
def Doubt():
    g=input("Enter The Name:")
    print("\t")
    l7.append(g)
    e=input("Enter The Subject:")
    print("\t")
    l8.append(e)
    f=input("Enter The Describtion:")
    print("\t")
    l9.append(f)
    print("Your Request has been Successfully Recorded And You will be Called by Your GFM Soon...")
    print("\t")

def Update():
    e=input("Enter Which Personal Information would You Like to Update?:")
    print("\t")
    if(e=="N" or e=="n"):
        f=input("Enter The New Name:")
        print("\t")
        for i in range(0,len(l)):
            if(l[i]==c):
                l[i]=c
                print("Record Updated Successfully..")
                print("\t")
                
    elif(e=="P" or e=="p"):
        f=input("Enter The New Name:")
        print("\t")
        for i in range(0,len(l)):
            if(l1[i]==c):
                l1[i]=c
                print("Record Updated Successfully..")
                print("\t")
    else:
        print("Sorry Enter Valid Option..")
        print("\t")

            
print("Hello User...")
print("\t")
h=input("Would you Like to Use The GFM Management System? (Enter Yes or No):")
print("\t")
while(h=="Y" or h=="y"or h=="Yes"):
    a=input("With whom's Profile would you like to Log In? (Enter Student or Teacher):")
    print("\t")
    if(a=="s" or a=="S"or a=="Student"):
        print("Hello Student")
        print("\t")
        print("Would you like to Register or Log In?:")
        print("\t")
        b=input("Enter:")
        print("\t")
        if(b=="R" or b=="r" or b=="Register"):
            c=input("Enter Name:")
            print("\t")
            l.append(c)
            print("\t")
            d=input("Enter Password:")
            l1.append(d)
            print("\t")
            print("Registration Complete")
            print("\t")
            
        if (b=="L" or b=="l" or b=="Login"):
            c=input("Enter Name:")
            print("\t")
            d=input("Enter Password:")
            print("\t")
            for i in range(0,len(l)):
                if (l[i]==c) and (l1[i]==d):
                    print("Log Inn Successfull")
                    print("\t")
                    z=input("Would you like to  perform Operations? (Enter Yes or No):")
                    print("\t")
                    while (z=="Y" or z=="y" or z=="Yes"):
                        print("Enter Which Operations would you like to perform?:")
                        print("\t")
                        print("1.Doubt \t 2.Help! \t 3.Update Your Record")
                        print("\t")
                        y=input("Enter:")
                        print("\t")
                        if (y=="H" or y=="h" or y=="Help"):
                                Help()
                        elif (y=="U" or y=="u" or y=="Update"):
                            Update()
                        elif (y=="D" or y=="d" or y=="Doubt"):
                            Doubt()
                        else:
                            print("Thank You..")
                            print("\t")
                            break
                else:
                    print("Invalid Credintials...\U0001F612")
                    print("\t")


    if(a=="t" or a=="T" or a=="Teacher"):
            print("Welcome Teacher")
            print("\t")
            print("Would you like to Register or Log In?:")
            print("\t")
            b=input("Enter:")
            print("\t")
            if(b=="R" or b=="r" or b=="Register"):
                c=input("Enter Name:")
                print("\t")
                l2.append(c)
                d=input("Enter Password:")
                print("\t")
                l3.append(d)
                print("Registration Complete...")
                print("\t")
                
            if (b=="L" or b=="l" or b=="Login"):
                c=input("Enter Name:")
                print("\t")
                d=input("Enter Password:")
                print("\t")
                for i in range(0,len(l2)):
                    if(l2[i]==c) and (l3[i]==d):
                        print("Log Inn Successfull")
                        print("\t")

                        z=input("Would you like to  perform Operations? (Enter Yes or No):")
                        print("\t")
                        while (z=="Y" or z=="y" or z=="Yes"):
                            print("Enter Which Operations would you like to perform?:")
                            print("\t")
                            print("1.Doubt \t 2.Help! \t 3.Update Your Record \t 4.Display \t 5.Enter Attendance")
                            print("\t")
                            y=input("Enter:")
                            print("\t")
                            if (y=="H" or y=="h"):
                                help_T()
                            elif (y=="D" or y=="d" or y=="Doubt"):
                                doubt_T()
                            elif (y=="U" or y=="u" or y=="Update"):
                                update_T()
                            elif (y=="Display" or y=="S"):
                                Display()
                            elif (y=="A" or y=="Attendance"):
                                P()
                            else:
                                print("Thank You For Using GFM Management System See You Soon...\U0001F601")
                                print("\t")
                                break

                    else:
                        print("Invalid Credintials...\U0001F612")
                        print("\t")


