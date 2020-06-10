import random
import sys

print("Hello, what is your name")
name = input()
print("Hello " + name + "! I am thinking to guess a number from 1 to 20")
secret_number = random.randint(1,21)
print("Guess the number")

for number_of_guesses in range(1,7):
    input_number = input()
    if int(input_number) > 20:
        print("Enter number only between 1 to 20")
        sys.exit()
    elif int(input_number) > secret_number:
        print("Number is too high")
    elif int(input_number) < secret_number:
        print("Number is too low")
    else:
        break

if int(input_number) == secret_number:
    print("Very Good! You have guessed in " + str(number_of_guesses) + " tries. Secret number is " + str(secret_number))
else:
    print("Nope! The secret number is " + str(secret_number) + "!Better luck next time")
        
