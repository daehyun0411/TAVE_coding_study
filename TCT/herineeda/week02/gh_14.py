from itertools import combinations

n,m = map(int, input().split())

matrix = []

chicken=[]

for i in range(n):
    temp=list(map[int, input().split()])
    matrix.append(temp)
    for j in range(n): #temp의 크기만큼 돌기
        if matrix[i][j] ==2: #치킨집
            chicken.append((i,j))
            
combi = []

for i in combinations(chicken,m):
    combi.append(i)

#combi 즉 치킨집 조합에 따라 만들어준다.
#distance를 만들고 distance는 치킨집의 조합일 때의 거리로 계산
#result를 이용해서 distance의 최소값 지속적으로 갱신

#for 문을 4번 사용
#1. combi를 결정하는데 사용 몇번째 조합인지
#2. matrix의 행을 결정
#3. matrix의 열을 결정
#4. 선택한 combi내에서 각 치킨집 사이의 거리를 각각 구해서 최소값으로 갱신

 INF = int(1e9) #갱신할 수 있도록
 result = INF
 
 for k in range(len(combi)):
    distance = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] ==1:
                res=INF
                for l in range(m):
                    x_dis = abs(i-combi[k][l][0])
                    y_dis = abs(i-combi[k][l][1])
                    res = min(res,y_dis+x_dis)
                distance+=res
                
    result = min(result,res)
    
print(result)
                
        
