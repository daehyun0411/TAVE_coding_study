from collections import deque

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
#모든 도로정보 입력받기
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
#모든 도시에 대한 최단 거리 초기화
distance = [-1 for _ in range(n+1)] 
# distance라는 거리 정보를 답은 배열을 -1로 초기화 한다.
# 탐색시 -1의 값은 아직 방문하지 않은 노드(도시)이다.
q = deque([x])
distance[x] = 0

# 그리고 문제 설명에서 출발 도시 X에서 X로 가는 최단거리는 항상 0이니
# distance[x] = 0으로 초기화 해준다.

while q:
    now = q.popleft()
    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            q.append(i)
# 탐색을 하면서 방문하지 않은 다음 도시(i)에 현재 탐색중인(now)의 거리 +1을 넣어 준다.

cnt = 0
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        cnt += 1
# distance를 조사하여 k와 같은 값이면 출력 k와 같은 값이 하나도 없다면 -1을 출력한다.
if not cnt:
    print(-1)
#시간초과 ..
