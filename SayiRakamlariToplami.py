number=int(input('Enter a number:'))
sumOfDigits=0
quotient=0
while number>=1:
    sumOfDigits=sumOfDigits+number%10
    number=number//10
    quotient=quotient+1
print("Sum of digits=",sumOfDigits)
print("Average of digits=",sumOfDigits/quotient)

