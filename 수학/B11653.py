n = int(input())

if n == 1:
    print("")

def factorization(x):
    d = 2

    while d <= x:
        if x % d == 0:
            print(d)
            x = x / d
        else:
            d = d + 1

factorization(n)   
