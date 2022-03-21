import math

alfabe=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',"A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sayilar=[0,1,2,3,4,5,6,7,8,9]


def isdigit(number):
    try:
        a=int(number)
        return True
    except:#integer ile yakalanamayan her şey bu hataya düşecektir.Biz de bu hatayı arıyoruz.
        return False
def isalpha(string):
    if string in alfabe:
        return True
    return False
alftosayi = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7


}
def SatirSayisiAl():
    print("Kare Kapan oyunu başlatılıyor.")
    durum = "yaratılmadı"
    satirsayisi = 0
    while (durum == "yaratılmadı"):

        print('Satır sayısı giriniz : ' , end=" ")
        satir = (input())
        if isdigit(satir):

           satirsayisi=int(satir)
        else:
            satirsayisi=-1
        if (isdigit(satirsayisi)):

            if (satirsayisi > 2) and (satirsayisi < 8):
                durum = "yaratıldı"
            else:
                print("Hatalı giriş satır sayısı, satır sayısı 3 ile 7 arasında girilmelidir.")
        else:
            print("Hatalı giriş lütfen sayı giriniz.")
    return satirsayisi

def MasaOlusturucu(satirsayisi):
    sutunsayisi=satirsayisi+1
    masa=[]
    for i in range(satirsayisi):
        boslist=[]
        for j in range(sutunsayisi):
            boslist.append(0)
        masa.append(boslist)

    return  masa

def MasaGoruntusu(masa):
    satirsayisi=len(masa)
    sutunsayisi=satirsayisi+1
    harfler=list(alftosayi.keys())
    print(end="  ")
    for i in range(sutunsayisi):

        print(harfler[i],end="   ")
    print()

    for i in range(satirsayisi):
        print(i+1,end=" ")
        for j in range(sutunsayisi-1):
            print(masa[i][j], end="---")
        print(masa[i][sutunsayisi-1],i+1)
        print(end="  ")
        if (i+1!=satirsayisi):

            for j in range(sutunsayisi-1):
                print("|",end="   ")
            print("|")
        else:

            for i in range(sutunsayisi):
                print(harfler[i], end="   ")
            print()

def UygunHamle (hamle):
    durum=0
    if isdigit((hamle[0])):
        durum+=1
    if isalpha(hamle[1]):
        durum+=1

    if durum==2:
        return True

    return False
def MasadaMı(masa,hamle):
    sutunSayisi=len(masa)+1
    satirSayisi=len(masa)
    hamleSatirIndexi=int(hamle[0])-1
    hamleSutunIndexi=alftosayi.get(hamle[1])
    if(hamleSutunIndexi==None):
        hamleSutunIndexi=-1
    puan=0
    if (satirSayisi>hamleSatirIndexi and hamleSatirIndexi>=0):
        puan+=1

    if (sutunSayisi > hamleSutunIndexi and hamleSutunIndexi >= 0):
        puan += 1
    if (puan==2):
        return True

    return False
def MasaDoldur(masa):
    maxTasSayisi=len(masa)*(len(masa)+1)
    tasSayisi=0
    while (tasSayisi<maxTasSayisi):
        if (tasSayisi%2)==0:
            print("Beyaz için ",end="")
        else:
            print("Siyah için", end="")


        print('hamlenizi  giriniz : ', end=" ")
        hamle = str(input())
        print()
        if not (len(hamle)==2):
           hamle="8Z"
        if UygunHamle(hamle):
            if MasadaMı(masa,hamle):


                satir=int(hamle[0])-1
                sutun=alftosayi[hamle[1]]

                if (masa[satir][sutun]!="B"and masa[satir][sutun]!="S"):

                    if (tasSayisi%2)==0:

                        masa[satir][sutun] = "B"


                    else:
                        masa[satir][sutun] = "S"

                    MasaGoruntusu(masa)
                    tasSayisi += 1
                else:
                    print("Masa içerisindeki bir hamle yapınız.")

            else:
                print("Masada değil, yeniden giriniz.")
        else:
            print("Uygun hamle değil.Yeniden giriniz.")
def KareleriBul(masa):
    siyahKareler=[]
    beyazKareler=[]
    for i in range(len(masa)):
        for j in range(len(masa)+1):
            deger=masa[i][j]
            try:
                if deger==masa[i+1][j] and deger==masa[i][j+1] and deger==masa[i+1][j+1] :
                    kareKordinatlari = [[i,j],[i+1,j],[i,j+1],[i+1,j+1]]

                    if deger=="B":

                        beyazKareler.append(kareKordinatlari)
                    else:
                        siyahKareler.append(kareKordinatlari)
            except:
                pass#out of bound err için
    return [beyazKareler,siyahKareler]
def HareketIslemi(masa,beyaz):

    while True:
        print("Hareket işlemi:")
        if (beyaz==1) :
            print("Beyaz için ", end="")
        else:
            print("Siyah için", end="")

        print('hamlenizi  giriniz : ', end=" ")
        hamle = str(input())
        print()
        hamleSkoru = 0
        if(len(hamle)==5):
            hamle1=hamle[0:3]
            hamle2=hamle[3:]
            if  UygunHamle(hamle1):
                hamleSkoru+=1
            if UygunHamle(hamle2):
                hamleSkoru+=1

        if hamleSkoru!=2:
            print("Hatalı hamle girişi, lütfen yeniden giriniz.")

        else: #Hareket geçerli bir hareket, masa için kontrollerini yapmak lazım.


            if (MasadaMı(masa,hamle1) and MasadaMı(masa,hamle2)):
                #Renge göre hareket ettirilecek,hareket ettirilen hedef dolu mu değil mi
                #Hareket birer birim uzaklıkta mı,eskisini de sıfırla
                hamle1X=int(hamle1[0])-1
                hamle1Y=alftosayi.get(hamle1[1])
                hamle2X = int(hamle2[0]) - 1
                hamle2Y = alftosayi.get(hamle2[1])
                if math.sqrt(pow(hamle2X - hamle1X, 2) + pow(hamle2Y - hamle1Y, 2)) == 1:

                    if (beyaz==1 and masa[hamle1X][hamle1Y]=="B" and masa[hamle2X][hamle2Y]=="0"):
                        masa[hamle1X][hamle1Y]="0"
                        masa[hamle2X][hamle2Y]="B"
                        break
                    if (beyaz == 0 and masa[hamle1X][hamle1Y] == "S"and masa[hamle2X][hamle2Y]=="0"):
                        masa[hamle1X][hamle1Y] = "0"
                        masa[hamle2X][hamle2Y] = "S"
                        break
                    print("Renk uyumsuzluğu var,tekrar deneyiniz.")
                else:

                    print("Hedef geçersiz.")


            else:
                print("Lütfen masada olan bir hareket giriniz.")


def KarelerinIcındeMi(kareler,koordinat):
    for i in range(len(kareler)):
        for j in range(4):
            if (kareler[i][j][0]==koordinat[0]and kareler[i][j][1]==koordinat[1] ):
                return False

    return True
def Cıkarma(masa,kareler,renk):
    beyazkareler=kareler[0]
    siyahkareler=kareler[1]
    while True:
        print("Çıkarma işlemi:")
        if (renk == 1):
            print("Beyaz için ", end="")
        else:
            print("Siyah için", end="")

        print('hamlenizi  giriniz : ', end=" ")
        hamle = str(input())
        print()
        if (UygunHamle(hamle)):
            hamle1X = int(hamle[0]) - 1
            hamle1Y = alftosayi.get(hamle[1])
            if (MasadaMı(masa, hamle)):


                if (renk== 1 and masa[hamle1X][hamle1Y] == "S"):
                    if  KarelerinIcındeMi(siyahkareler,[hamle1X,hamle1Y]):

                        masa[hamle1X][hamle1Y] = "0"
                        break
                if (renk == 0 and masa[hamle1X][hamle1Y] == "B"):
                    if KarelerinIcındeMi(beyazkareler, [hamle1X, hamle1Y]):
                        masa[hamle1X][hamle1Y] = "0"
                        break
                print("Renk uyumsuzluğu var ya da hedef boş tekrar deneyiniz.")
            else:

                print("Hamle masada değil.")


        else:
            print("Hatalı hamle girişi, lütfen yeniden giriniz.")


def AnaOyun(masa):
    tasSayisi=len(masa)*(len(masa)+1)
    siyahTasSayisi=tasSayisi/2
    beyazTasSayisi=siyahTasSayisi
    beyazKareSayisi=0
    siyahKareSayisi=0
    round=0


    while(siyahTasSayisi>3 and beyazTasSayisi>3):
        kareler=KareleriBul(masa)
        beyazKareSayisi=len(kareler[0])
        siyahKareSayisi=len(kareler[1])


        if (round%2)==1: #Hareket ettirme evresi
            HareketIslemi(masa,1)
            MasaGoruntusu(masa)
            HareketIslemi(masa,0)
            MasaGoruntusu(masa)
        else: #Artık çıkarma işlemi yapılır.
            if (beyazKareSayisi > 0 or siyahKareSayisi>0):

                for i in range(len(kareler[0])):
                    Cıkarma(masa,kareler,1)
                    siyahTasSayisi-=1
                    MasaGoruntusu(masa)
                if (siyahTasSayisi>3): # Siyah taşlar beyazdan önce biteceği için siyahlar bittiyseprogramın devam etmesine gerek yoktur.

                    for i in range(len(kareler[1])):
                        Cıkarma(masa,kareler,0)
                        beyazTasSayisi-=1
                        MasaGoruntusu(masa)

            else:
                if(round==0):
                    if (siyahKareSayisi==0 and beyazKareSayisi==0): #İki rengin de karesi yoksa birer tane taş çıkartılır .
                        Cıkarma(masa,kareler,1)
                        siyahTasSayisi-=1
                        MasaGoruntusu(masa)
                        Cıkarma(masa,kareler,0)
                        beyazTasSayisi=beyazTasSayisi-1
                        MasaGoruntusu(masa)
        round+=1
    if (beyazTasSayisi!=3):
        print("Beyaz kazandı.")
    else:
        print("Siyah kazandı.")







def KareKapan (name):
    satirsayisi=SatirSayisiAl()
    masa=MasaOlusturucu(satirsayisi) #Gerekli iki boyutlu diziyi oluşturduk.
    MasaGoruntusu(masa)
    MasaDoldur(masa)
    AnaOyun(masa)




if __name__ == '__main__':
    KareKapan ('PyCharm')



