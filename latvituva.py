def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
answer = factorial(num)

print("The factorial of ", num, "is", answer)