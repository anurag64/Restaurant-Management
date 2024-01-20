import random
def items1():
    print('='*100)
    print(' '*30,'Items list',' '*30)
    print('='*100)
    fp=open("items.txt","r")
    contents=fp.readlines()
    for i in contents:
        i=i.rstrip().split(',')
        print(i[0],'-->',i[1],'-->',i[2])
    l=[]
    s=[]
    total=0
    while True:
        flag=0
        dish=input("\nEnter dish no:\n")
        qty=int(input("Enter quantity no:\n"))
        ch=input("Hit 'y' to continue:\n")
        for i in contents:
            i=i.rstrip().split(',')
            if(dish==i[0]):
                flag=1
                l=[i[1],qty]
                price=int(i[2])*qty
                total+=price
                s.append(l)
        if(flag==0):
            print("Dish not available!")
        if ch!="y":
            break
    print("------------Your order------------\n")
    order=random.randint(100,1000)+random.randint(200,2000)
    print(f"Your order no is:{order}\n")
    for i in s:
        print(i[0],"--",i[1])
    print(f"\n########### Your Order Total Amount is:{total}##########\n")
    ch1=input("Hit a 'y' to confirm your order:\n")
    if ch1=='y':
        for i in s:
                print(i[0],"-",i[1])
                l=str(order)+","+i[0]+","+str(i[1])+"\n"
                f = open("orderlist.txt","a")
                f.writelines(l)
                f.close()
    else:
        print("\nLog in again to place a new order!\nHave a nice day sir.")