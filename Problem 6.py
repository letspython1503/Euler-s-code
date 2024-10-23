def sumSquareDifference(n):
    final1=(n*(n+1)*((2*n)+1)) / 6
    final2= ((n*(n+1))/2)**2
    return abs(int(final1-final2))
n=int(input('Enter the number'))
print(sumSquareDifference(n))