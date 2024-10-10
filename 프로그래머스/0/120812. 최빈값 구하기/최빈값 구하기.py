def solution(array):
    temp_dict = {}
    
    # 딕셔너리 생성하고 각 개수 세기
    for i in array:
        if i in temp_dict:
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1

    max_count = 0
    max_index = -1
    
    # 딕셔너리를 순회하면서 최빈값 찾기
    for key, value in temp_dict.items():
        if value > max_count:
            max_count = value
            max_index = key
        elif value == max_count:
            max_index = -1  # 최빈값이 여러 개일 경우

    return max_index
