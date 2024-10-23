import math
def is_Prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def sum_of_Primes(n1):
    sum1 = 0
    for i in range(1,n1+1):
        if is_Prime(i):
            sum1 += i
    return sum1
    
z = int(input("Enter required Number: "))
print(sum_of_Primes(z))
