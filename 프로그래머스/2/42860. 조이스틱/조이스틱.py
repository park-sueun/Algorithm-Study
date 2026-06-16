# 문제: 주어진 이름을 만드는 최소 조작 횟수
# 이 문제는 문자 변경 비용과 커서 이동 비용으로 나눌 수 있다
# 문자 변경은 위아래 이동 중 더 작은 값을 선택하면 된다.

# 커서 이동은 단순히 오른쪽으로 이동하는 것이 최적이 아니다.
# 연속된 A 구간이 존재하면 방향을 전환하여 
# 해당 구간을 건너뛰는 것이 더 유리할 수 있다.

# 따라서 각 위치에서 연속된 A 구간을 탐색하고,
# 방향 전환 시의 이동 횟수를 계산하여 최소 이동 수를 구하겠습니다.

def solution(name):
    
    answer = 0
    n = len(name)
    
    move = n - 1
    
    for i, c in enumerate(name):
        answer += min(
            ord(c) - ord('A'),
            ord('Z') - ord(c) + 1 # 특정 알파벳부터 Z까지 조작 횟수 + A에서 Z 조작 횟수(1)
        )
        
        next_idx = i + 1
        
        # 연속된 A 구간을 지나 다음 idx 찾기
        while (
            next_idx < n and name[next_idx] == 'A'
        ):
            next_idx += 1
            
        # 커서를 좌우로 이동하는 최소 횟수
        move = min(
            move, # 끝에서 끝까지
            i * 2 + (n - next_idx), # 오른쪽으로 이동
            i + 2 * (n - next_idx) # 왼쪽으로 이동
        )
            
    return answer + move