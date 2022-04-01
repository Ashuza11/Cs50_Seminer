# Guessing a number between 1 and 10 and 
# Give feedback to the user.
import random

number = random.randint(1, 10)

def main():
    print("*************************************")
    print("Hello world this is the guessing Game")
    print("*************************************")
    guessing(number)

    print("***** Thank you for playing the Game *****")


def guessing(n):
    for i in range(3):
        n = int(input("Number: "))

        # Evaluate the guessing 
        if n < number:
            print("Number is too small")
        elif n > number:
            print("Number is to larger")
        else:
            print("Bingo your guess the correct number")
   
main()