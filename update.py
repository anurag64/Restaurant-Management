def itemslist():
    print("press 1 to add item")
    print("press 2 to delete item")
    print("press 3 to change price")
    ch=input("select-> ")
    if ch=='1':
        add_list()
    elif ch=='2':
        delete_list()
    elif ch=='3':
        update_price()
    else:
        print('Invalid input')

def add_list():
    quant=input("Enter the item no you want to add:\n")
    name=input("Enter the name of the item\n")
    price=input("Enter the price\n")
    l=[]
    detail= quant +','+ name +',' + price + '\n'
    l.append(detail)
    f=open("items.txt","a")
    f.writelines(l)
    f.close

def delete_list():
    while True:
        flag=0
        fp = open("items.txt",'r')
        dishes = fp.readlines()
        num = input("Enter the item no you want to delete:")
    
        
        for i in range(len(dishes)):
            k = dishes[i].rstrip().split(',')
            if k[0]==num:
               dishes[i]=""
               flag=1
        if flag==0:
             print("The item number do not exist choose another item number")
             continue
        else:
             print("-"*20,"Item deleted successfully","-"*20)
             fp=open("items.txt","w")
             fp.writelines(dishes)
             fp.close()
             break

def update_price():
    while True:
        flag=0
        fp = open("items.txt",'r')
        dishes = fp.readlines()
        num=input("Enter the item no: ")
        value=input("enter the price you want to update:")
        for i in range(len(dishes)):

            k=dishes[i].rstrip().split(",")
            if k[0]==num:
                dishes[i]=k[0]+","+k[1]+","+value+"\n"
                flag=1
        if flag==0:
            print("The item number do not exist choose another item number")
            continue
        else:
            print("-"*20,"price updated successfully","-"*20)
            fp=open("items.txt","w")
            fp.writelines(dishes)
            fp.close()
            break