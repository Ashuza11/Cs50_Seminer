# # CountDown for new year.
# for i in range(10):
#     print(10 - i)

# # print("Happy New Year!")


# The same solution using Fucntions 
# def main():
#     countdown()
#     print("Happy New Year!")


# def countdown():
#     for i in range(10):
#         print(10 - i)

# main()

# Ameliorated solution
import random
import time

def main():
    number = random.randint(5, 15)
    countdown(number)
    print("Happy New Year!")


def countdown(n):
    for i in range(n):
        print(n - i)
        time.sleep(1)

main()
