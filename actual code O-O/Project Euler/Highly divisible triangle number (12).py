num = 1
amntofdivisors = 0
def isTriangular(n):
    for i in range(1,n):
        if (i*(i+1))/2 == n:
            return True
    return False

while amntofdivisors < 500:
    num = num + 1
    if isTriangular(num):
        amntofdivisors = amntofdivisors + 1
        print(f"amnt of divisors {amntofdivisors}")
print(num)