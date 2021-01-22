'''
https://programmers.co.kr/learn/courses/30/lessons/49191
n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다.
권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다.
심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.
선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.n	results	return

n   results                                     return
5	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	2
'''
from collections import defaultdict

def solution(n, results):
    # dfs해서 자식 노드의 개수를 반환하는 코드
    def dfs(start, graph):
        stack = [start]
        visited = []
        child = 0
        while stack:
            i = stack.pop()
            if i not in visited:
                child += 1
                visited.append(i)
                for j in graph[i]:
                    stack.append(j)
        return child-1 # 자기 자신 제외



    win_graph = defaultdict(list)   # key: winner, value: 내가 이긴 대상
    lose_graph = defaultdict(list)  # key: loser,  value: 내가 진 대상
    for winner, loser in results:
        win_graph[winner].append(loser)
        lose_graph[loser].append(winner)

    answer = 0
    for i in range(1, n+1):
        if dfs(i, win_graph)+dfs(i, lose_graph) == n-1:
            answer += 1
    return answer

if __name__ == "__main__":
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    n = 5
    solution(n, results)
