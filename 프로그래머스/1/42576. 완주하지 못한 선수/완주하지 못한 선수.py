# 문제 정의: 참가자(n) - 완주자(n - 1) = 완주하지 못한 선수(1)의 이름을 반환하라 
# - 동명이인이 있을 수 있음

# 시간복잡도: 단순 중첩 for문(O(N^2)) 1000까지는 감당 가능 / 이름 조회 성능을 보장하기 위해 O(1) - dict를 사용하겠습니다.

from collections import Counter
def solution(participant, completion):
    # 참가자 이름의 등장 횟수를 저장
    # 완주자 이름이 나올 때마다 갯수를 감소시킵니다.
    # 마지막에 개수가 1인 사람이 완주하지 못한 사람입니다.
    
    # 방법 1
#     participant_dict = {}
    
#     for name in participant:
#         if not name in participant_dict:
#             participant_dict[name] = 0
#         participant_dict[name] += 1
    
#     for name in completion:
#         participant_dict[name] -= 1
        
#     for name, count in participant_dict.items():
#         if count > 0:
#             return name

    
    # 방법 2
    return list(Counter(participant) - Counter(completion))[0]
    
    
    
    
    