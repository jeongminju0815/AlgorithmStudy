n , k = map(int, input().split())
arr = list(input())

stack = []
count = 0

stack.append(arr[0])
for i in range(1,n):
    while stack and stack[-1] < arr[i] and count<k:
        print("w",stack)
        stack.pop()
        count+=1
    stack.append(arr[i])
    print(stack)
if count!=k:
    print("".join(stack[:len(stack)-(k-count)]))
else:   
    print("".join(stack))
    