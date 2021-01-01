class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i+1 for i in range(n)]
        return list(itertools.combinations(arr, k))
        # 굳이 arr를 생성하지 않고 바로 range로 iterator 객체를 넘겨주는 게 메모리 사용에 있어서 더 나을 듯.
