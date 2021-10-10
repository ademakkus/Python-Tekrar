number=int(input('Enter a pattern rows:'))
for i in range(1,number+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(end='\n')
print("-----------------------------------")
number=int(input('Enter a pattern rows:'))
for i in range(number+1,1,-1):
    for j in range(1,i):
        print(j,end=" ")
    print(end='\n')
