'''
https://leetcode.com/problems/reconstruct-itinerary/
'''
from typing import List
from collections import defaultdict, deque


# 이해 XX ....
# https://leetcode.com/problems/reconstruct-itinerary/discuss/375397/Simply-simple-Python-Solution-Using-stack-for-dfs-with-comments
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from_to_dict = defaultdict(list)
        for src, trg in tickets:
            from_to_dict[src].append(trg)

        for key in from_to_dict.keys():
            from_to_dict[key].sort(reverse=True)  # pop연산의 효율성을 위해

        result = []
        stack = ["JFK"]
        while len(stack) > 0:
            elem = stack[-1]
            if elem in from_to_dict and len(from_to_dict[elem]) > 0:
                stack.append(from_to_dict[elem].pop())
            else:
                # elem not in from_to_dict or
                # len(from_to_dict[elem]) == 0
                # 이 공항에 도착하면 더이상 가지 못하기 때문에 result에 append (나중에 리턴할 때 역순으로 해서 리턴)
                # 이해 X ...
                result.append(stack.pop())
        return result[::-1]


if __name__ == "__main__":
    solution = Solution()
    #result = solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    #print(result)

    result = solution.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])
    print(result)

