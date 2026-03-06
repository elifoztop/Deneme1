import  random
menu=1
while menu==1:
    s=[]
    o=[]
    b=[]
    X=[]
    temp=[]
    analist=[]
    glist=[]
    m=float(input("Oyun alanı boyutu giriniz(10-20 arası giriş yapınız): "))
    if 10<=m<=20:
        tuzak=m*m*0.2
        hazine=m*m*0.15
        shazine=hazine*0.5
        ohazine=hazine*0.3
        bhazine=hazine*0.2
        for i in range(int(shazine)):
            s.append("s")
        for i in range(int(ohazine)):
            o.append("o")
        for i in range(int(bhazine)):
            b.append("b")
        for i in range(int(tuzak)):
            X.append("X")
        list=s+o+b+X
        while len(list)!=int(m*m):
            list.append(".")
        kontrol=0
        random.shuffle(list)
        for i in list:
            temp.append(i)
            kontrol=kontrol+1
            if kontrol==int(m):
                analist.append(temp.copy())
                temp.clear()
                kontrol=0
        temp.clear()
        for j in range(int(m)):
            for t in range(int(m)):
                temp.append("?")
            glist.append(temp.copy())
            temp.clear()
    else:
        print("Hatalı giriş")
        continue