def owner(ch):
    if ch=="2":
        pw=input("Enter your password:\n")
        if pw=="Owner@123":
            print("**********What do you want to do**********")
            print("\t1.Update item list\n\t2.Dispatch order\n\t3.View the item list\n\t4.Exit\n")
            ch1=input("Enter your choice:\n")
            if ch1=='1':
                import update
                update.itemslist()
            elif ch1=='2':
                import order
                order.dispatch()
            elif ch1=='3':
                print("--MENU--")
                fp=open("items.txt",'r')
                print(fp.read())
                fp.close()
            elif ch1=='4':
                exit()