print('*** Finding the largest number in the list.*******')
list = [1,2,3,45,6,7,8,8,34,32,55,83,233,12,3,4,5,8,9,0,0,0,2,444,5]
maxNumber=-999999999999999999
for i in range(len(list)):
    if maxNumber<list[i]:
        maxNumber=list[i]
        print("i=",i," max number =",maxNumber)
print("max number=",maxNumber)