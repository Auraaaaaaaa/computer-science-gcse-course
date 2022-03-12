n1, n2 = 0, 1
count = 0
print("Fibonacci sequence:")
while n1 <=4000000:
    if n1 % 2 == 0:
        print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
print("Finished!")