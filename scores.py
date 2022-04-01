# # Score bars
# def main():
#     score1 = int(input("Scor1: "))
#     scor2 = int(input("Scor2: "))
#     scor3 = int(input("Scor3: "))

#     for i in range(score1):
#         print("#", end="")
#     print()

#     for i in range(scor2):
#         print("#", end="")
#     print()

#     for i in range(scor3):
#         print("#", end="")
#     print()

# main()

## Improvement using fuctions 

def main():
    score1 = int(input("Scor1: "))
    score2 = int(input("Scor2: "))
    score3 = int(input("Scor3: "))

    print_score(score1)
    print_score(score2)
    print_score(score3)

   
def print_score(n):
    for i in range(n):
        print("#", end="")
    print()

main()
