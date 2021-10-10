print("******Çarpanlarına Ayırma*****")
sayi=int(input("Enter a number:"))
for i in range(sayi):
    if sayi%(i+1)==0:
        print(i+1,end=" ")
