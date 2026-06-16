# 문제정의 : (0, 0) -> (n-1, m-1) 까지 최단 거리 문제. 상하좌우 한칸 -> 1 가중치 X, 도착하지 못할 수 있음(-1)
# 알고리즘 선택 : BFS -> 가까운 노드부터 탐색하므로 도착 지점에 처음 도달한 거리가 최단 거리입니다.
# 시간복잡도 : 맵의 크기 O(N*M) 각 칸 방문 최대 1회
# 질문: DFS가 안되는 이유 -> 한번 가면 돌아올 필요가 없지만 DFS는 돌아옴, 한번에 끝까지 갔다가 와서 비효율적임

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    directions = [
        (0, -1), (0, 1), (-1, 0), (1,0)
    ]
    
    # BFS 큐에 무엇을 넣을 것인가 -> 현재 위치
    
    q = deque()
    q.append((0, 0))
    
    while q:
        # 이미 방문한 곳은 다시 방문하지 않는다.
        # 벽은 이동할 수 없다.
        # 격자를 벗어날 수 없다.
        
        x, y = q.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            
            if maps[nx][ny] == 0:
                continue
                
            if maps[nx][ny] != 1:
                continue
                
            # 방문(현재 칸까지의 이동거리)
            maps[nx][ny] = maps[x][y] + 1
            
            q.append((nx, ny))
            
    return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1
        
        