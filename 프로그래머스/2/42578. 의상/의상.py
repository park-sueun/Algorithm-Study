# 조합, 종류별 최대 1가지, 전날과 하나만 겹치지 않으면 됌, dict() 크기는 1이상
def solution(clothes):
    # 옷을 종류별로 분류 -> key value 쌍 -> dict
    c_dict = {}
    for c in clothes:
        c_dict[c[1]] = c_dict.get(c[1], 0) + 1
        
    print(c_dict)
        
    # 조합(nCr)
    total = 1
    for v in c_dict.values():
        total = total * (v + 1)
    return total - 1 # 아무것도 안입는 경우