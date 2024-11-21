n = int(input("Enter a number: "))

num = 1
while num <= n:
    factorial = num
    i = 1
    while i < num:
        factorial *= i
        i += 1
    print(f"{num}! = {factorial}")
    num += 1