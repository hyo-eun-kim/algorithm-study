# quicksort python implementation
def quicksort(A, low, high):
    """
    재귀형태로 구현
    """
    def partition(low, high): # 함수 안에 함수를 넣어주기 때문에 변수를 공유함.
    # 따라서 A를 인자로 전달해줄 필요가 없음
        pivot = A[high]
        left = low
        # left, right은 최종적으로 pivot 왼쪽에 위치할 곳과 오른쪽에 위치할 곳에 대한 indicator
        for right in range(low, high):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left] # swap
                left += 1
        A[left], A[high] = A[high], A[left] # pivot을 left, right 가운데로 옮김 (partition)
        # pivot의 위치가 맨 오른쪽에서 현재 left가 가리키고 있는 위치로 변경됨
        return left # pivot의 위치를 return함

    if low < high: # 재귀 호출 조건
        pivot = partition(low, high)
        quicksort(A, low, pivot-1)
        quicksort(A, pivot+1, high)
