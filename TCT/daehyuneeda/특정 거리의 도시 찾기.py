# 간선의 비용이 일정할 때 너비우선탐색(BFS)
from collections import deque

# 도시, 도로, 거리, 출발 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 도로 정보 입력
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    
distance = [-1] * (n+1)
distance[x] = 0

#BFS
q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단거리가 k인 모든 도시 번호 출력            
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
        
# 없다면 -1   
if check == False:
    print(-1)   