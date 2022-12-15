n = int(input())
edge = list(map(int, input().split()))
node = list(map(int, input().split()))

min_node = node[0]
cost = 0 

for i in range(len(edge)):
    if node[i] < min_node:
        min_node = node[i]
    cost += (min_node * edge[i])
print(cost)
        

    