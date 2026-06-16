# 문제 해석: 이 문제는 컴퓨터 간 연결 관계가 주어지고, 서로 연결된 그룹의 개수를 구하는 문제입니ㅏㄷ.
# - 연결 관계를 그래프로 해석할 수 있으며, 결국 연결 요소(Connected Component)의 개수를 구하는 문제라고 생각합니다.
# 알고리즘: 따라서 DFS 또는 BFS를 사용해 탐색할 수 있습니다. -> DFS를 탐색할 것 -> 하나의 연결관계를 모두 찾으면 그 관계에 속한 애들은 더 이상 접근하지 않아도 된다.
# 시간복잡도: 인접 행렬을 사용하고 있으므로 O(N * N)

def solution(n, computers):
    visited = [False] * n
    count = 0
    
    def dfs(node):
        visited[node] = True
        
        for next_node in range(n):
            # 이미 방문한 노드
            if visited[next_node]:
                continue
            
            # 연결되어 않는 경우
            if computers[node][next_node] == 0:
                continue
                
            dfs(next_node)
        
        # 네트워크 연결 끝
        
    for node in range(n):
        if not visited[node]:
            dfs(node)
            count += 1
            
    return count
        
    