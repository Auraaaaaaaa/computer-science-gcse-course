import math
def isprime(num):
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        return False
    else:
      return True

nua=int(input("enter a number"))

num = int(math.sqrt(nua))

factors=[]
for i in range(1,num+1):
    if num%i==0:
       if num % 1 == 0:
            if isprime(i):
                factors.append(i)
                print(i)
            else:
                print(f"Not: {i}")

print ("Factors of {} = {}".format(num,factors))
