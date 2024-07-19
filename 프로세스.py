#풀이 : https://velog.io/@xxooxx99/4-Algorithm-%EC%8B%A4%ED%96%89-%EB%8C%80%EA%B8%B0-%ED%81%90%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%EA%B4%80

from collections import deque

def solution(priorities, location):
    # 각 프로세스의 우선순위와 원래 인덱스를 저장하는 큐 생성
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    answer = 0  # 실행 순서를 기록할 변수
    
    while queue:
        # 큐에서 첫 번째 프로세스를 꺼냄
        current = queue.popleft()
        
        # 현재 프로세스보다 높은 우선순위가 있는지 확인
        if any(current[0] < item[0] for item in queue):
            # 높은 우선순위가 있으면 현재 프로세스를 다시 큐에 넣음
            queue.append(current)
        else:
            # 높은 우선순위가 없으면 현재 프로세스를 실행
            answer += 1
            if current[1] == location:
                return answer

#EXPLAINATION
# queue 변수에 주어진 우선순위와 인덱스를 함께 저장한 deque를 생성한다. 이는 각 프로세스의 우선순위와 원래 위치를 추적하기 위함이다.
# while 루프를 이용해 큐가 빌 때까지 반복한다.
# current 변수에 큐의 가장 앞에 있는 프로세스를 저장하고, 큐에서 제거한다.
# if any(current[0] < item[0] for item in queue): 조건문을 이용해 큐에 현재 프로세스보다 우선순위가 높은 프로세스가 있는지 확인한다.
# 만약 있다면, 현재 프로세스를 다시 큐에 추가한다.
# 만약 없다면, 현재 프로세스를 실행하고 answer 값을 1 증가시킨다. 이때, 실행한 프로세스가 우리가 찾는 프로세스인지 확인하고 맞다면 answer 값을 반환한다.

#TEST
print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))  
