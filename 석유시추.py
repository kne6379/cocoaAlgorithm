##pseudocode
##DFS와 BFS를 사용, 석유 덩어리 찾기
##각 열을 순회하면서, 해당 열을 통과하는 석유덩어리 크기 합산, 각 열에 대하여 시추관을 설치했을때 얻을 수 있는 석유량을 저장
def find_oil_clusters(land):
    n, m = len(land),len(land[0]) # 땅의 크기를 정의 #len(land)는 행의갯수를. len(land[0]) 는 열의 갯수(첫번째 행)
    cluster_map = [[-1] * m for _ in range(n)] #각 위치에 클러스터(석유가 있는 군집) 인덱스를 저장할 배열을 초기화
    clusters = [] #각 클러스터의 크기를 저장할 리스트를 초기화함
    cluster_index = 0 # 클러스터 인덱스를 초기화

    def dfs(x, y):
        stack = [(x, y)] #DFS를 위한 스택을 초기화
        size = 0 # 현재 클러스터의 크기를 초기화
        while stack:
            cx, cy = stack.pop() #스택에서 현재 위치를 꺼냄
            if 0 <= cx < n and 0 <= cy < m and land[cx][cy] == 1:
                land[cx][cy] = -1  # 방문 표시 
                cluster_map[cx][cy] = cluster_index #클러스터 인덱스를 기록
                size += 1 #클러스터 크기를 증가
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #상하좌우 방향으로 이동
                    stack.append((cx + dx, cy + dy)) #스택에 새로운 위치를 추가
        return size #현재 클러스터의 크기를 반환

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                cluster_size = dfs(i, j) #새로운 클러스터를 발견하면 DFS를 수행
                clusters.append(cluster_size) #클러스터의 크기를 리스트에 추가
                cluster_index += 1 #클러스터 인덱스를 증가

    return clusters, cluster_map #클러스터 크기와 클러스터 맵을 반환

def calculate_oil_by_column(land, clusters, cluster_map):
    n, m = len(land), len(land[0]) #땅의 크기를 저장
    max_oil = 0 # 최대 석유량을 저장할 변수를 초기화

    for col in range(m):
        visited_clusters = set() #이미 방문한 클러스터를 위한 집합을 초기화
        oil_amount = 0 #현재 열에서 얻을수 있는 석유랑 초기화
        for row in range(n):
            if cluster_map[row][col] != -1: #클러스터가 있는지 확인
                cluster_idx = cluster_map[row][col] #클러스터 인덱스를 가져옴
                if cluster_idx not in visited_clusters: #해당 클러스터를 이미 방문했는지 확인
                    oil_amount += clusters[cluster_idx] #석유량을더함
                    visited_clusters.add(cluster_idx) #방문한 클러스터를 집합에 추가
        max_oil = max(max_oil, oil_amount) # 최대 석유량 갱신
    
    return max_oil #최대 석유량을 반환

def solution(land):
    clusters, cluster_map = find_oil_clusters(land) #클러스터 크기와 클러스터 맵을 찾는다
    return calculate_oil_by_column(land, clusters, cluster_map) # 최대 석유량을 계산

# 예제 테스트
land1 = [
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1]
]

land2 = [
    [1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1]
]

print(solution(land1))  
print(solution(land2))  
