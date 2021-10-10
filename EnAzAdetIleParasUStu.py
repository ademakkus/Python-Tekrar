harcama=int(input('Yaptığınız harcama miktarı:'))
verilenPara=int(input('Verilen para:'))
fark=verilenPara-harcama
yuzluk=0
ellilik=0
yirmilik=0
beslik=0
birlik=0
onluk=0
yeniFark=0
katsayi=0
if fark==0:
    print('Para üstü yok.')
if fark<0:
    print(abs(fark)," kadar daha para veriniz ")
    yeniFark=int(input('Yeni tutar :'))
    fark = yeniFark-fark
if fark > 100:
        katsayi = fark // 100
        fark = fark - (fark // 100) * 100
        yuzluk = yuzluk + katsayi
if fark > 50:
        katsayi = fark // 50
        fark = fark - (fark // 50) * 50
        ellilik = ellilik + katsayi
if fark > 20:
        katsayi = fark // 20
        fark = fark - (fark // 20) * 20
        yirmilik = yirmilik+katsayi
if fark > 10:
        katsayi = fark // 10
        fark = fark - (fark // 10) * 10
        onluk = onluk+katsayi
if fark>0:
        katsayi = fark // 1
        fark = fark - (fark // 1)*1
        birlik =birlik+ katsayi

print('Para üstü :',yuzluk,' adet 100 TL,',ellilik,' adet 50 TL,',yirmilik,' adet 20 TL,',onluk,' adet 10 TL,',beslik,
      ' adet 5 TL,',birlik,' adet 1 TL')
