import random
n=random.randrange(1,50)
guess=int(input("enter any number:"))
while n!=guess:
    if guess < n:
        print("too low")
        guess=int(input("enter any number:"))
    elif guess > n:
        print("too high")
        guess=int(input("enter any number:"))
    else:
        break
print("you guessed it right")