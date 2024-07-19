import math

def solution(progresses, speeds):
    answer = []
    days_left = []

    # 각 기능이 완료되기까지 남은 일수를 계산
    for progress, speed in zip(progresses, speeds):
        days = math.ceil((100 - progress) / speed)
        days_left.append(days)

    # 첫 번째 기능의 배포 일수 설정
    current_deploy_day = days_left[0]
    count = 1
    
    # 남은 기능들에 대해 배포 일수를 계산
    for day in days_left[1:]:
        if day <= current_deploy_day:
            # 현재 배포 일수 내에 완료되는 기능이라면 배포 카운트 증가
            count += 1
        else:
            # 현재 배포 일수를 넘어서 완료되는 기능이라면 지금까지의 카운트 저장하고 배포 일수 갱신
            answer.append(count)
            current_deploy_day = day
            count = 1

    # 마지막 배포 일수에 대한 기능 수를 저장
    answer.append(count)

    return answer

# 예시 실행
print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]
