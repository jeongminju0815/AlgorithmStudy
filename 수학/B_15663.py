n, m = map(int, input().split())
num = list(map(int,input().split()))

num.sort()

result = []
def choice(i, temp):
    if len(temp) == m:
        if temp not in result:
            print(" ".join(map(str,temp)))
            
        result.append(temp)
        return
    for j in range(n):
        if j!= i:
            choice(j,temp+[num[j]])


for i in range(len(num)):
    choice(i,[num[i]])


    