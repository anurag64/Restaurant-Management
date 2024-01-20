def dispatch():
    while True:
        flag=0
        l=[]
        f = open("orderlist.txt","r")
        dsp = f.readlines()
        for i in range(len(dsp)):
            k = dsp[i].rstrip().split(',')
            print(f"{k[0]}--->{k[1]}--->{k[2]}")
        dis=input("Enter the order number:\n")
        for i in range(len(dsp)):
            k = dsp[i].rstrip().split(',')
            if k[0]==dis:
                dsp[i]=""
                flag=1
        if flag==0:
            print("The order number do not exist choose another item number")
            continue
        else:
            print("-"*20,f"Order no :{dis} dispatched","-"*20)
            fp=open("orderlist.txt","w")
            fp.writelines(dsp)
            fp.close()
            break