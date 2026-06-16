def solution(tickets):
    # 인접리스트(트리, 단방향, 경로가 2개인 경우 알파벳 순 탐색)
    # 각 티켓 사용 여부 관리
    
    tickets.sort()
    
    used = [False] * len(tickets)
    answer = []
    
    print(tickets)
    
    def dfs(curr, path):
        nonlocal answer
        
        if answer:
            return
        
        if len(path) == len(tickets) + 1:
            answer = path[:]
            return
        
        for i in range(len(tickets)):
            start, end = tickets[i]
            
            if used[i]: # 이미 사용된 티켓
                continue
            
            if start != curr:
                continue
            
            used[i] = True
            dfs(end, path + [end])
            used[i] = False
            
    dfs("ICN", ["ICN"])
    return answer
        
    
    
    