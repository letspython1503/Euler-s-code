import math
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
def nthPrime(n):
    count=0
    a=1
    while True:
        if is_prime(a):
            count+=1
        if count==n:
            return a
        a+=1
z=int(input('Enter your number'))
print(nthPrime(z))
