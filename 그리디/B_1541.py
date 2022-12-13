s = input().split("-")

result = 0

for i in range(len(s)):
    _result = 0
    for j in s[i].split("+"):
        _result += int(j)

    if i == 0:
        result += _result
        continue
    
    result -= _result
print(result)