n, m = map(int, input().split())
arr = list(map(int,input().split()))

arr.sort()

def sequence(n, temp):
    if len(temp) == m:
        print(' '.join(map(str,temp)))
        return
    
    for i in range(n,len(arr)): #인덱스로 접근하여 중복 방지, n : 탐색 중인 인덱스
        sequence(i,temp+[arr[i]])
        

sequence(0,[])
#(0,[]) -> (0,[1])  
#                 -> (0,[1,1]) -> (0,[1,7]) -> (0,[1,8]) ->(0,[1,9])
#       -> (1,[]) -> (1,[7]) 
#                              -> (1,[7,7]) -> (1,[7,8])