from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
opt_num = list(map(int, input().split())) #["+", "-", "*", "//"]
opt = ["+", "-", "*", "//"]
opt_total = []

for i in range(len(opt_num)):
    if opt_num[i] == 0:
        continue
    for j in range(opt_num[i]):
        opt_total.append(opt[i])

total = list(set(permutations(opt_total, n-1)))
nmax = -1e10
nmin = 1e10
operation = []

for o in range(len(total)):
    temp = 0
    for i in range(len(arr)):
        if i == 0:
            temp = eval(str(arr[i])+total[o][i]+str(arr[i+1]))
        elif i == n-1:
            continue
        else:
            if temp < 0 and total[o][i] == "//":
                temp = abs(temp)
                temp = eval(str(temp)+total[o][i]+str(arr[i+1]))
                temp = -temp
            else:
                temp = eval(str(temp)+total[o][i]+str(arr[i+1]))
    if nmax < temp:
        nmax = temp
    if nmin > temp:
        nmin = temp 
print(nmax)
print(nmin)
