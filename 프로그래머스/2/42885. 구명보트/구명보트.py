# 문제 정의: 한 번에 최대 2명씩, 무게 제한, 구명보트를 최소한으로 사용하여 모든 사람을 구출하는 방법

def solution(people, limit):
    # 가장 무거운 사람부터 체크(가장 무거운 사람 + 가장 가벼운 사람 > limit: 가장 무거운 사람은 혼자 타야함)
    # 정렬 후 투포인터를 사용하여 O(N)에 해결
    
    people.sort()
    print(people)
    
    answer = 0
    left, right = [0, len(people)-1]
    while left < right:
            
        if people[left] + people[right] > limit:
            # 가장 무거운 사람만 태운다
            answer += 1
            right -= 1
            continue
            
        if people[left] + people[right] <= limit:
            # i랑 j랑 둘다 태우는 경우
            answer += 1
            left += 1
            right -= 1
            continue
            
    if left == right:
        # 한 사람이 남은 경우
        answer += 1
        
    return answer