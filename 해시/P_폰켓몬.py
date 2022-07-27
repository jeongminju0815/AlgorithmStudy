def solution(nums):
    answer = 0
    count = int(len(nums) / 2)
    check = 0
    max_num = max(nums)
    min_num = min(nums)
    
    dic = {i:0 for i in range(min_num,max_num+1)}
    
    for i in nums:
        dic[i] += 1
        
    for key,value in dic.items():
        if value == 0:
            check += 1
    
    if len(dic)-check > count:
        answer = count
    else:
        answer = len(dic)-check
         
    return answer