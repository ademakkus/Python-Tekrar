number=int(input('Enter a number:'))
for i in range(2,number):
    if number%i==0:
        isPrime=False
        break
    else:
        isPrime=True
if isPrime:
    print("{} is prime ".format(number))
else:
    print("{} is NOT prime ".format(number))

#prime numbers between two numbers
lower = 100
upper = 500
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)