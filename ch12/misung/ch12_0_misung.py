graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3],
}

### 깊이 우선 탐색 (DFS)
def dfs(v,discovered=[]):  # discovered 에는 탐색한 노드를 저장한다.
    discovered.append(v)

    for w in graph[v]:  
        if not w in discovered:
            discovered = dfs(w,discovered)  # w가 탐색한 노드가 아니라면, 탐색한다!
    return discovered

print(dfs(1))  # [1,2,5,6,7,3,4]


### stack 을 이용한 DFS
def stack_dfs(start):
    discovered = []
    stack=[start]
    while stack:
        v=stack.pop()  # 맨 마지막 원소가 pop 되겠죠? stack은 Last in First out
        if v not in discovered:  # 노드를 탐색하지 않았다면, discovered 에 추가하고 탐색한다.
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

print(stack_dfs(1))  # [1, 4, 3, 5, 7, 6, 2]

## 같은 DFS 이지만 순서가 다르다!
## 왜? stack 으로 구현한건 마지막에 삽입된 노드부터 꺼내서 반복하기 때문이당


### Queue 를 이용한 너비우선 탐색 (BFS) => 다익스트라 알고리즘 등에 매우 유용하게 쓰인다
def bfs(start):
    discovered=[start]
    queue=[start]
    while queue:
        v=queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

print(bfs(1))  # [1, 2, 3, 4, 5, 6, 7]

### 백트래킹 : 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 후보를 포기해 정답을 찾아가는 방법

