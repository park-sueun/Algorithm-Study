# 한 번호가 다른 번호의 접두어가 있으면 false, 없으면 true
# for 문을 사용하게 되면 O(phone_book(N) * len(M))  = 2000000 -> 비효율적
# set을 사용하겠습니다. -> 동일한 번호가 있는 경우 false 리턴

def solution(phone_book):
    # 정렬을 이용하면 접두사가 되는 문자열들이 서로 붙어 있게 됨
    phone_book.sort()
    
    for i in range(len(phone_book) - 1): # 시간복잡도: O(N)
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
        
    return True