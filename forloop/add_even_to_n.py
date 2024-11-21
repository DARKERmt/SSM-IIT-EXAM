n = int(input("Enter a number : "))
sum = 0
for i in range(1,1+n):
    if i % 2 == 0:
        sum = sum+i
print(f"The sum of the following numbers is {sum}")