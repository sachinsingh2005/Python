# Enter a number and prints factorial of that number

# using for loop
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)


# using while loop
num = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print("Factorial of", num, "is", factorial)


# using recursion
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
