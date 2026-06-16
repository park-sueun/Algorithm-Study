# 문제정의: 과학자의 H-index 구하기
# h번 이상 인용된 논문이 최소 h편 이상이면 그 중 최대 h
def solution(citations):
    
    # 인용 횟수를 내림차순 정렬하면 i번째 위치의 논문은 적어도 i편의 논문보다 인용 횟수가 높다는 의미가 됩니다.
    # 따라서 citations[i] >= i + 1 인 가장 큰 값을 찾으면 그것이 H-Index
    
    citations.sort(reverse=True)
    
    for i, citation in enumerate(citations):
        if citations[i] < i + 1:
            return i
        
    return len(citations)
        