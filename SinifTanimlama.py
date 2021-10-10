class Ogrenci:
    def __init__(self,numara,ad,soyad,sinif):
        self.ad=ad
        self.soyad=soyad
        self.numara=numara
        self.sinif=sinif
        self.derslistesi=[]
    def dersEkle(self,ders):
        self.derslistesi.append(ders)

class Hoca:
    def __init__(self,ad,soyad):
        self.ad=ad
        self.soyad=soyad
        self.verdigiDersler=[]
    def dersEkle(self,ders):
        self.verdigiDersler.append(ders)
class Ders:
    def __init__(self,kod,ad,hoca=None):
        self.kod=kod
        self.ad=ad
        self.hoca=hoca
        self.ogrenciListesi=[]
    def hocayiBelirle(self,hoca):
        self.hoca=hoca
    def ogrenciEkle(self,ogrenci):
        self.ogrenciListesi.append(ogrenci)
    def dersBilgisiYazdir(self):
        print("Ders kodu:",self.kod)
        print("Ders Adı:",self.ad)
        print("Ders Hocası:",self.hoca.ad,self.hoca.soyad)
        print(self.ad,"Öğrenci Listesi")
        for ogrenci in self.ogrenciListesi:
            print(ogrenci.ad+" "+ogrenci.soyad)
    print("---------------------------------------------------")
furkan=Ogrenci(1234,"Furkan","AKKUŞ",4)
aysenur=Ogrenci(12345,"Ayşenur","AKKUŞ",3)
kerem=Ogrenci(23456,"Kerem","AKKUŞ",1)
yusuf=Ogrenci(34567,"Yusuf","AKKUŞ",4)
ademHoca=Hoca("Adem","AKKUŞ")
gultenHoca=Hoca("Gülten","AKKUŞ")

programlama=Ders("PRG102","Programlama Temelleri")
edebiyat=Ders("EDB203","Türk Dili ve Edebiyatı")
yazilim=Ders("YZM400","Yazılım Mühendisliği Giriş")
programlama.hocayiBelirle(ademHoca)
edebiyat.hocayiBelirle(gultenHoca)
yazilim.hocayiBelirle(ademHoca)
furkan.dersEkle(programlama)
furkan.dersEkle(edebiyat)
furkan.dersEkle(yazilim)

kerem.dersEkle(programlama)
kerem.dersEkle(edebiyat)

aysenur.dersEkle(yazilim)
aysenur.dersEkle(edebiyat)


programlama.ogrenciEkle(furkan)
programlama.ogrenciEkle(kerem)

edebiyat.ogrenciEkle(furkan)
edebiyat.ogrenciEkle(kerem)
edebiyat.ogrenciEkle(aysenur)
yazilim.ogrenciEkle(kerem)
print("***Ders Bilgilerini Yazdırma***")
programlama.dersBilgisiYazdir()
edebiyat.dersBilgisiYazdir()
yazilim.dersBilgisiYazdir()

