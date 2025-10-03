import random

greet = "welcome to the game"
x = greet.capitalize()

print(x)
print("guess the number between 1 - 10!!!")

random_number = random.randint(1,10)

while True:
    try:
        guess = int(input("input any number"))

        if guess < random_number:
            print("too low")
        elif guess > random_number:
            print("too high")
        else:
            print("u won")
            break

    except ValueError:
        print("input the valid number")