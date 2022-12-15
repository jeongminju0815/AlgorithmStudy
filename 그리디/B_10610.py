n = input()

total = 0
arr = []
flag = False
for i in n:
    if i == '0':
        flag = True
    total += int(i)
    arr.append(i)

if not flag:
    print(-1)
else:
    if total % 3 == 0:
        arr.sort(reverse=True)
        print("".join(arr))
    else:
        print(-1)



