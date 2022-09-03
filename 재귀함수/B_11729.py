def f(n, start, end, sub):
    if(n == 1):
        print(start, sub, sep = " ")
    else:
        f(n-1, start, sub, end)
        f(1, start, end, sub)
        f(n-1, end, start, sub)

n = int(input())
print(2**n-1)
if(n <= 20):
  f(n, 1, 2, 3)