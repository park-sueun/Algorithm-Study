def solution(numbers, target):
    
    # dfs
    # 각 레벨은 numbers의 숫자 하나를 의미
    # 왼쪽은 +, 오른쪽은 -
    # 리프노드 total == target: 1 else 0
    
    def dfs(idx, total):
        # base case
        if idx == len(numbers):
            return 1 if total == target else 0
        
        return (
            dfs(idx + 1, total + numbers[idx])
            + # 전체 갯수 
            dfs(idx + 1, total - numbers[idx])
        )
    
    return dfs(0, 0)
    