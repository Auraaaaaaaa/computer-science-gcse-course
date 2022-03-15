
def ispalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

num1 = 1
num2 = 1
tstring = ""
while num1 and num2 <100000:
    target = num1 * num2
    tstring = str(target)
    half1 = tstring[:len(tstring)//2]
    half2 = tstring[len(tstring)//2]
    if ispalindrome(tstring):
        print(f"Palindrome: {tstring}. Num1: {num1} Num2: {num2}")
    num1 = num1 + 1
    num2 = num2 + 1
