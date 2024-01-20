def login(ch):
    if ch=="1":
        print("====================Welcome Customer====================")
        print("1.New customer")
        print("2.Existing customer")
        ch1=input("Login as:")
        if ch1=="1":
            while True:
                print("Enter new customer details:")
                name=input("Enter name of the new customer:")
                pas=input("Enter password of the new customer:")
                def password(pas):
                    spe=["@","#","$"]
                    val=True
    
                    if len(pas)<6:
                        print("at least 6 ch")
                        val=False
                    elif not any (char.isdigit() for char in pas):
                        print("at least one digit")
                        val=False
                    elif not any (char.isupper() for char in pas):
                        print("at least one capital")
                        val=False
                    elif not any(char.islower() for char in pas):
                        print("at least one small")
                        val=False
                    elif not any(char in spe for char in pas):
                        print("at least one sp")
                        val=False
                    if val:
                        return val
                if(password(pas)):
                    l=[]
                    details=name+','+pas+'\n'
                    l.append(details)
                    f=open("Customers.txt","a")
                    f.writelines(l)
                    f.close
                    ch=input("Hit y to continue").lower()
                    if ch!='y':
                        break
        elif ch1=="2":
            print("Welcome customer!")
            name1=input("Enter your name:")
            fp=open('Customers.txt','r')
            contents=fp.readlines()
            fp.close()
            flag=0
            for i in contents:
                i=i.rstrip().split(',')
                if(i[0]==name1):
                    flag=1
                    pas1=input("Enter your password:")
                    while(i[1]!=pas1):
                        print("Wrong password.")
                        pas1=input("Enter your password:")
                    if(i[1]==pas1):
                        print("Login successful.")
                        import items
                        items.items1()
                    
            if(flag==0):
                print("User doesn't exist.")
                        
            
           
    elif ch=="2":
        print("====================Welcome Owner====================")
    else:
        print("Invalid choice")