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
    if isPrime(num):
        numbers.append(num)
        if len(str(num)) > 1:
            if isPrime(int(str(num)[:-1])):
                if isPrime(int(str(num)[1:])):
                    finished = True
