#recursive
def faktoriyelHesapla(number):
    if number < 0:
        print('Factorial cannot be calculated.')
        return 1
    elif number == 1:
        return 1
    else:
        return number * faktoriyelHesapla(number - 1)
#iterative
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

number = int(input('Enter a number:'))
result=faktoriyelHesapla(number)
print("Recursive {} sayısının faktöriyeli :{}".format(number, result))
result2=factorial(number)
print("İterative {} sayısının faktöriyeli :{}".format(number, result2))