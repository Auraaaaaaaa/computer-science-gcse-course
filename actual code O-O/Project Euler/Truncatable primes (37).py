def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numbers = []
num = 2
finished = False
while not finished:
    if (isPrime(num)):
        numbers = [int(d) for d in str(num)]
        if (all(isPrime(int(d))) for d in str(num)) and (all(isPrime(int(d))) for d in str(num)[::-1]):
            print(num)
            finished = True