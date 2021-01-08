#네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 
# 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 
# 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 
# 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

#컴퓨터의 개수 n, 
#연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

def solution(n, computers):
    def dfs(v, n):
        visited[v] = True # dfs 가 호출된순간 일단 방문한거로 바꾸기
        
        for i in range(n): # 그리고 컴퓨터 수만큼 확인
            if computers[v][i] and not visited[i]: # v컴퓨터랑 다른컴퓨터가 연결이 되어있고, 방문하지 않았으면,
                dfs(i, n)  # dfs
    
    count = 0
    visited = [False] * n # 컴퓨터 대수만큼 빈 공간 만들기
    
    for i in range(n):  # 컴퓨터 대수 만큼 돌면서 
        if not visited[i]:  # i 번째를 방분하지 않았으면, dfs
            dfs(i, n)
            count += 1  # 네트워크수 증가
    
    return count