import switch as switch

"""number=int(input('Enter a number between 1-100: '))
while number>99 or number<1:
    number = int(input('Enter a number between 1-100: '))
    """
for i in range(1,100):
    number=i
    onesDigit = number % 10
    tensDigit = number // 10
    if tensDigit == 1:
        stringNumber = "On"
    if tensDigit == 2:
        stringNumber = "Yirmi"

    if tensDigit == 3:
        stringNumber = "Otuz"
    if tensDigit == 4:
        stringNumber = "Kırk"
    if tensDigit == 5:
        stringNumber = "Elli"
    if tensDigit == 6:
        stringNumber = "Altmış"
    if tensDigit==0:
        stringNumber=""
    if tensDigit == 7:
        stringNumber = "Yetmiş"
    if tensDigit == 8:
        stringNumber = "Seksen"
    if tensDigit == 9:
        stringNumber = "Doksan"
    if onesDigit == 1:
        stringNumber += " bir"
    if onesDigit == 2:
        stringNumber += " iki"
    if onesDigit == 3:
        stringNumber += " üç"
    if onesDigit == 4:
        stringNumber += " dört"
    if onesDigit == 5:
        stringNumber += " beş"
    if onesDigit == 6:
        stringNumber += " altı"

    if onesDigit == 7:
        stringNumber += " yedi"
    if onesDigit == 8:
        stringNumber += " sekiz"
    if onesDigit == 9:
        stringNumber += " dokuz"
    print('Sayı : ', number, ' okunuşu:', stringNumber)