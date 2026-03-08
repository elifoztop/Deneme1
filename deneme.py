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
        for i in range(0,int(m+1)):
            temp.append(str(i))
        glist.append(temp.copy())
        temp.clear()
        kontrol2=0
        for j in range(int(m)):
            kontrol2=kontrol2+1
            temp.append(str(kontrol2))
            for t in range(int(m)):
                temp.append("?")
            glist.append(temp.copy())
            temp.clear()
        #//////////////////////////////////
        secilen=[]
        can=3
        puan=0
        acık=int(input("Açık modu oyunun başlamadan görmek istiyorsanız 1 tuşlayınız: "))
        buluntu=0
        if acık==1:
            for i in analist:
                print(i)
        while can>0 and buluntu!=int(hazine):
            h=0
            t=0
            print("===  HAZİNE AVCISI  ===")
            print(f"Hazine Sayısı: {int(hazine)} / Tuzak Sayısı: {int(tuzak)} / CAN: {can}")
            for i in glist:
                print(i)
            satir = int(input(f"Satır no giriniz(1-{int(m)}): "))
            if satir<1 or satir>m:
                print("Hatalı Giriş.Tekrar Deneyiniz.")
                continue
            sutun = int(input(f"Sütun no giriniz(1-{int(m)}): "))
            if sutun<1 or sutun>m:
                print("Hatalı Giriş.Tekrar Deneyiniz.")
                continue
            temp2=str(satir)+str(sutun)
            if temp2 not in secilen:
                secilen.append(temp2)
                for i in range(satir-2,satir+1,):
                    for j in range(sutun-2,sutun+1):
                        if -1<i<m and -1<j<m:
                            if analist[i][j] == ".":
                                pass
                            elif analist[i][j] == "X":
                                t += 1
                            elif analist[i][j] == "s":
                                h += 1
                            elif analist[i][j] == "o":
                                h += 1
                            elif analist[i][j] == "b":
                                h += 1
                if analist[satir - 1][sutun - 1] == ".":
                    print(f"Boş Hücre! T:{t} H:{h}")
                    glist[satir][sutun] = analist[satir - 1][sutun - 1]
                elif analist[satir - 1][sutun - 1] == "X":
                    print(f"Tuzak! CAN-1! T:{t-1} H:{h}")
                    can=can-1
                    glist[satir][sutun] = analist[satir - 1][sutun - 1]
                elif analist[satir - 1][sutun - 1] == "s":
                    print(f"Küçük Hazine! T:{t} H:{h-1}")
                    puan=puan+1
                    glist[satir][sutun] = analist[satir - 1][sutun - 1]
                elif analist[satir - 1][sutun - 1] == "o":
                    print(f"Orta Hazine! T:{t} H:{h-1}")
                    puan=puan+3
                    glist[satir][sutun] = analist[satir - 1][sutun - 1]
                else:
                    print(f"Büyük Hazine! T:{t} H:{h-1}")
                    puan=puan+5
                    glist[satir][sutun] = analist[satir - 1][sutun - 1]
            else:
                print("Bu alanı önceden seçtiniz.Tekrar Deneyiniz.")
        if buluntu==int(hazine):
            puan = puan - ((3 - can) * 2)
            print(f"!!!Tebrikler Tüm Hazineleri Buldunuz!!! PUAN: {puan}")
            menu=int(input("Cıkıs yapmak istiyorsanız 0 tuslayınız yoksa 1'i tuslayınız: "))
            if menu!=1 and menu!=0:
                print("Hatalı giriş")
                menu = int(input("Cıkıs yapmak istiyorsanız 0 tuslayınız yoksa 1'i tuslayınız: "))
        else:
            puan = puan - ((3 - can) * 2)
            print(f"Maalesef Kaybettiniz. PUAN: {puan}")
            menu = int(input("Cıkıs yapmak istiyorsanız 0 tuslayınız yoksa 1'i tuslayınız: "))
            if menu!=1 and menu!=0:
                print("Hatalı giriş")
                menu = int(input("Cıkıs yapmak istiyorsanız 0 tuslayınız yoksa 1'i tuslayınız: "))
    else:
        print("Hatalı giriş")