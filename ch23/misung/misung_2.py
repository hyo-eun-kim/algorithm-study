# 그리디 알고리즘
# 단속 카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884
# 고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.

# 고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 
# 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 
# return 하도록 solution 함수를 완성하세요.

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾습니다.

    for route in routes:
        if camera < route[0]: # 카메라보다 시작 지점이 먼저 앞에 있다는거니까 
            answer += 1
            camera = route[1]  # 카메라 설치
    return answer