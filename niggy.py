import random

ans = random.randint(1, 10)
tries = 0
while True:
    guess = int(input("Guess a number btw 1 and 10. "))
    tries += 1
    if guess == ans:
        print("Good job blud! ")
        break
    elif guess > ans:
        print("Too high blud! ")
    elif guess < ans:
        print("Too low blud! "
    else: print("Type valid!")
print("You took " +str(tries) +" tries! ")