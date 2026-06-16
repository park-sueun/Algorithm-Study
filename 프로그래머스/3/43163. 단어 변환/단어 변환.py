# 문제 설명: 이 문제는 begin에서 target까지 변환하는 최소 횟수를 구하는 문제입니다.
# - 각 단어를 노드로 생각하고, 한 글자만 다른 단어끼리 연결된 그래프로 볼 수 있습니다.
# 알고리즘: 모든 변환 비용이 동일하므로 최단 변환 횟수를 구하기 위해 BFS를 사용하겠습니다.

from collections import deque

def is_convertible(w1, w2):
    # 변환 가능한가
    diff_count = 0
    
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            diff_count += 1
    
    return diff_count == 1

def solution(begin, target, words):
    
    if target not in words:
        return 0

    visited = [False] * len(words)
    
    # 큐에는 현재 단어와, 변경횟수를 넣어 관리함
    q = deque([(begin, 0)])
    
    while q:
        curr, count = q.popleft()
        
        if (curr == target):
            return count
        
        for i in range(len(words)):
            next_word = words[i]
            
            if visited[i]:
                continue
                
            if not is_convertible(curr, next_word):
                continue
                
            visited[i] = True
            q.append((next_word, count + 1))
            
    return 0