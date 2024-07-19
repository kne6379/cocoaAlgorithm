#파이썬 행렬 다루기
#파이썬 dfs/bfs다루기
#DFS - 가능한 깊이까지 탐색을 계속하다가, 더 이상 깊이 갈 수 없으면 다음 경로를 탐색, 주로 스택(재귀 호출을 통해 암시적으로 사용)이나 
# 명시적인 스택 자료구조를 사용
#BFS - 현재 노드와 인접한 노드를 모두 탐색, 그 다음 인접노드를 탐색, 큐 자료구조를 사용


#파이썬 풀이
#논리 세우기
#행렬은 n*m, 이동형태는 좌표형식
#출발지(1,1)와 도착지(n,m)는 고정되어있음 - 출발지와 도착지에 대한 모든 경로 탐색 - 중간에 막혀있는지 확인- 경로탐색중 좌표 이동마다 count += 1 
#탐색된 경로중에 count 가 가장 작은 값 - 최단경로
#만약 (n,m)에 대하여 (n,m-1),(n,m),(n-1,m)의 좌표에 입력 matirx에 1이 들어가있으면 경로 count 상관없이 -1 리턴


#최단경로 - BFS 사용


from collections import deque #표준 라이브러리 ceollections 안에 잇는 deque 라이브러리를 사용 
#deque - double-ended-queue의 약자, queue를 사용하기 위해 사용
# 큐 채우기 - https://upload.wikimedia.org/wikipedia/commons/5/5d/Breadth-First-Search-Algorithm.gif

def solution(maps):
    #행(n) 열(m)의 크기 확인하기
    n=len(maps) #n(행)은 리스트의 갯수
    m=len(maps[0]) #m(열)은 리스트 내 요소 개수

    #방향 벡터 선언하기 (상,하,좌,우)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    #큐 초기화
    queue = deque([(0,0,0)]) # (좌표값- x,y,이동거리(0))
    maps[0][0] = 0 #시작 위치 설정, (0,0)을 시작위치로 방문 처리 하여 재방문하지 않도록 설정


    while queue: #큐가 비어있지 않다면 -> 탐색할 위치가 남아있다면 계속 반복
        x, y, dist = queue.popleft() #(큐에서 현재 위치와 이동거리 꺼내기)
        
        print(f"현재 위치: ({x}, {y}), 이동 거리: {dist}")

        if x == n - 1 and y == m - 1: #(0부터 시작하니까 -1)
            return dist + 1 #(목적지(n-1,m-1)에 도착하면 이동거리를 dist에 반환, 도착전까지의 dist만 반환하기 때문에, dist에 + 1 )
        
        for dx, dy in directions: #아까 선언한 방향벡터 directions를 이용하여 이동 위치 계산하기
            nx, ny = x + dx, y + dy #만약 현재 위치가 (x,y) =(3,4) 에서, 오른쪽으로 한칸(0,1) 이동한다고 하면, 새로운 위치는 (3,5)가 됨 해당 내용을 계산
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1: #새로운 위치(nx,ny)가 전체 행렬(n-1,m-1)안에 있고 해당 위치가 maps을 봤을때 1이라면,
                #1이면 벽이 없으니까 이동 가능
                queue.append((nx, ny, dist + 1)) #새로운 위치와 이동거리를 큐에 추가
                maps[nx][ny] = 0  # 이동한 위치를 방문 처리
    
    return -1 #큐가 빌때까지 목적지에 도달하지 못할경우  -1 반환

#추가 검색내용 - 큐가 빈다 -- BFS에서는 더이상 탐색할수없음
#큐가 차잇음- 아직 탐색할 위치가 남아잇음

maps1 = [[1, 0, 1, 1, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 0, 1],
         [0, 0, 0, 0, 1]]

maps2 = [[1, 0, 1, 1, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 0, 0],
         [0, 0, 0, 0, 1]]

print(solution(maps1))  
print(solution(maps2)) 
