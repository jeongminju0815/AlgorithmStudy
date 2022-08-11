def calculations(c, arr):
    num1 = arr.pop()
    num2 = arr.pop()
    if c == "+":
        op.append(num2 + num1)
    if c == "-":
        op.append(num2 - num1)
    if c == "*":
        op.append(num2 * num1)
    if c == "/":
        op.append(num2 / num1)
    
n = int(input())
notation = input()
dic = {}
op = []

for i in range(n):
    k = int(input())
    dic[chr(65+i)] = k

for i in notation:
    if i.isalpha():
        op.append(dic[i])
    else:
        calculations(i, op)
print("%.2f"%op[0])