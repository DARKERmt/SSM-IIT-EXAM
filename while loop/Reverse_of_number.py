num = int(input("Enter Your Number: "))
reverse = 0
original = num
while num>0:
    digit = num % 10
    reverse = reverse * 10 +  digit
    num = num // 10
print(reverse)
