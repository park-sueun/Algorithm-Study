from collections import deque

def solution(maps):
    # 시작점(0,0) -> 도착점(n-1, m-1)까지의 최단 거리
    # BFS를 활용
    # 최단 거리에 DFS를 안쓰는 이유
    # : 모든 경로를 다 탐색해야 함
    
    n = len(maps)
    m = len(maps[0])
    
    directions = [
        # 상하좌우
        (0, -1), (0, 1), (-1, 0), (1, 0)
    ]
    
    q = deque() # 시작점
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            # 범위를 벗어난 경우
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            
            # 벽(0) 이거나 이미 거쳐간 경우(> 1)
            if maps[nx][ny] != 1:
                continue;
                
            maps[nx][ny] = maps[x][y] + 1
            q.append((nx, ny))
            
    # maps가 > 1이면 도착 아니면 도착 못함
    return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1
                
    
    
    
    
    