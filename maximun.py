
def main():
    x = int(input("x: "))
    y = int(input("y: ")) 
    z = maximun(x, y)

    print("Maximum is", z)

def maximun(a, b):
    if a > b:
        return a
    else:
        return b

main()