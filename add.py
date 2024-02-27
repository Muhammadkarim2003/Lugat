import os
def inp():
    dic=dict()
    while True:
        l = open("lugat.txt", "a")
        a=open('lugat.txt','r')
        a=a.read()
        en = input("En ").capitalize()
        uz = input("Uz ").capitalize()
        a=a.split("\n")[:-1]
        for i in a:
            i=i.split(': ')
            dic[i[0]]=i[1]
        if en in dic:
            print("<<<Bu so'z mavjud🤷🏻>>>")
        else:
            l.write(f"{en}: {uz}\n")
        
        a=int(input("Yana so'z qo'shasizmi\n\t1.Ha\n\t0.Yo'q\n"))
        
        if a==1:
            continue
        else:
            l.close()
            os.system("cls")
            break
