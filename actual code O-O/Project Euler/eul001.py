num = 1
array = []

while num <=1000:
    if num % 3 == 0:
        array.append(num)
    
    elif num % 5 == 0:
        array.append(num)
    num = num + 1
total = sum(array)
print(total)