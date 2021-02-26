# 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681
# 네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 
# 그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다. 
# 다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.

def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        bin_str = bin(arr1[i] | arr2[i])[2:]  # 앞에 0b 제거
        ans.append(("0" *(n - len(bin_str)) + bin_str).replace("1", "#").replace("0", " "))  # 앞에 0 채워넣기
    return ans
