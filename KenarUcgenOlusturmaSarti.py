birinciKenar=int(input('Birinci kenar uzunluğunu giriniz:'))
ikinciKenar=int(input('İkinci kenar uzunluğunu giriniz:'))
ucuncuKenar=int(input('Üçüncü kenar uzunluğunu giriniz:'))
if abs(birinciKenar-ikinciKenar)<ucuncuKenar and (birinciKenar+ikinciKenar)>ucuncuKenar:
    result=True
elif abs(ikinciKenar-ucuncuKenar)<birinciKenar and (ikinciKenar+ucuncuKenar)>ucuncuKenar:
    result=True
elif abs(birinciKenar-ucuncuKenar)<ikinciKenar and (birinciKenar+ucuncuKenar)>ikinciKenar:
    result=True
else:
    result=False

if result:
     print('Üçgen olabilir.')
else:
     print('Üçgen OLAMAZ.')