def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic = {i:[] for i in id_list}
    
    for r in report:
        user , reported = r.split()
        dic[reported].append(user)
        
    for i in range(len(id_list)):
        if len(set(dic[id_list[i]])) >= k:
            for j in set(dic[id_list[i]]):
                answer[id_list.index(j)]+=1

    return answer

def resolution(id_list, report, k):
    answer = [0] * len(id_list)
    dic = {i : 0 for i in id_list}
    
    for r in set(report):
        dic[r.split()[1]] += 1
    for r in set(report):
        if dic[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    return answer


id_list = ["muzi", "frodo","apeach","neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(resolution(id_list, report, k))