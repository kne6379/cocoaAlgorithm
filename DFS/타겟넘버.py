# 순서를 바꾸지 않는다.
# target을 정해놓고, 해당 과정이 나올 수 있는 경우의 수를 출력해야한다
# 이럴라면 모든 경우의 수를 일단 컴퓨터한테 계산시켜놓고, 그중에조건문으로 출력해야겠다.
# 아 모든 경우의 수를 계산하기 만들때 DFS(깊이 우선 탐색)을 사용하네


def solution(numbers, target):
    def dfs(index, current_sum):
        # 기본 조건: 모든 숫자를 사용한 경우
        if index == len(numbers):
            # 현재 합계가 목표 값과 같다면 1을 반환, 그렇지 않으면 0을 반환(이과정에서 return 값을 출력해야한다)
            return 1 if current_sum == target else 0
        
        # 현재 숫자를 더하거나 빼는 두 가지 경우를 모두 탐색하여
        # 가능한 모든 경로를 재귀적으로 호출, #재귀적 호출이란? : 함수의 로직을 재사용한다

        # index + 1: 다음 숫자를 처리하기 위해 인덱스를 증가
        # current_sum + numbers[index]: 현재 숫자를 더한 경우
        # current_sum - numbers[index]: 현재 숫자를 뺀 경우

        add_case = dfs(index + 1, current_sum + numbers[index]) # 다음숫자를 처리하기 위해 인덱스 증가하고(다음 ),  
        subtract_case = dfs(index + 1, current_sum - numbers[index]) #case 추가 -1
        
        # 두 가지 경우의 수를 합산하여 반환
        return add_case + subtract_case

    # 초기 세팅
    return dfs(0, 0) 

# 테스트
print(solution([1, 1, 1, 1, 1], 3))  # 결과: 타겟 넘버를 만드는 방법의 수

#dfs(1,1) ->dfs(x,n) x는 인덱스 자리의 숫자를 나타내는게 아니라  x-1 자리의 숫자
