import math
def solution(n, k):
    answer = 0
    r = ""
    
    while n != 0:
        r = str(n % k) + r
        n = n // k
    
    numbers = [int(i) for i in r.split('0') if i!=""]
    
    
    for i in numbers:
        if i == 1:
            continue
        check = True
        for j in range(2, int(math.sqrt(i))+1):
            if i % j ==0:
                check = False
                break
        if check:
            answer +=1
    return answer