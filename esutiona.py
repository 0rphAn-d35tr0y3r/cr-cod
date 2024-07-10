def isgood(n):
    if n % 3 == 0:
        return True
    if n % 5 == 0:
        return True
    return False

ANS = 0

for i in range(1, 1000):
    if isgood(i):
        ANS += i

print(ANS)