def is_Prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
n= int(input('Enter the upper limit'))
sum1=2
for i in range(1,n,2):
    if is_Prime(i):
        sum1+=i
print(sum1)