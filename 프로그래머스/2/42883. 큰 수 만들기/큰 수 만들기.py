# k개의 숫자를 제거 후 얻을 수 있는 가장 큰 숫자를 구하는 문제
# 각 자리의 숫자를 리스트로 변경 > 순서를 지켜야 함.
def solution(number, k):
    
    # 더 큰 숫자가 뒤에 오면 현재 숫자는 지워도 됌
    
    stack = []
    
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        
        stack.append(num)
        
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)