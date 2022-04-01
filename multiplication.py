from numpy import product


def main():
    for i in range(10):
        for j in range(10):
            multily(i, j)
    
def multily(x, y):
    product = x * y
    print(x, "*", y ,"=", product)

main()