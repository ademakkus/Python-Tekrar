
"""
Okula haftanın 5 günü giden bir öğrenci hem gidiş için hem de dönüş için 3 er TL otobüs bileti vermektedi.
Ayrıca okulda olduğu günlerde yemekhaneden 6 TL'ye yemek yemektedir. Öğrencinin günlük, haftalık ve aylık masrafı ne kadardır?
"""
bilet=int(input('Bilet parası :'))
yemek=int(input('Yemek parası :'))
gunSayisi=int(input('Haftada Okula Gittiği Gün Sayıs :'))


gunSayisi=5
gunlukHarcama= yemek + 2 * bilet
haftalikHarcama= gunSayisi * gunlukHarcama
aylikHarcama=4*haftalikHarcama
print("Günlük Harcama :",gunlukHarcama)
print("-------------------------------")
print("Haftalık Harcama :",haftalikHarcama)
print("-------------------------------")
print("Atlık Harcama :",aylikHarcama)
