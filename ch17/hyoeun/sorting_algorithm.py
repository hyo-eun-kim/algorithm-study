# O(n^2)
def bubble_sort(unsorted_list: list):
    print("before: ", unsorted_list)
    for i in range(len(unsorted_list)):
        for j in range(0, len(unsorted_list)-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    print("after: ", unsorted_list)


# O(NlogN)
def merge_sort(unsorted_list: list):
    def merge(left, right):
        sorted_list = []
        left_index = 0
        right_index = 0
        while (left_index < len(left)) and (right_index < len(right)):
            if left[left_index] <= right[right_index]:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1
        while left_index < len(left):
            sorted_list.append(left[left_index])
            left_index += 1
        while right_index < len(right):
            sorted_list.append(right[right_index])
            right_index += 1
        return sorted_list

    if len(unsorted_list) == 1:
        return unsorted_list
    mid = len(unsorted_list)//2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    divided_left = merge_sort(left)
    divided_right = merge_sort(right)
    return merge(divided_left, divided_right)


def quick_sort(unsorted_list, low, high):
    def partition(low, high):
        # 가장 오른쪽에 있는 숫자를 피봇으로 선택한다.
        # 사실, 퀵소트에서는 하나의 숫자를 랜덤으로 선택하나, 코드상의 편의상 가장 오른쪽의 값을 선택한 것으로 보인다.
        pivot = unsorted_list[high]
        # 가장 왼쪽 수에 left marker를 표시
        left = low
        # 가장 오른쪽 수에 right marker를 표시
        right = high-1
        while left < right:
            # low는 pivot보다 더 큰 수가 나올때까지 이동
            while unsorted_list[left] < pivot:
                left += 1
            while unsorted_list[right] > pivot and right > left:
                right -= 1
            if left < right:
                unsorted_list[left], unsorted_list[right] = unsorted_list[right], unsorted_list[left]

        if unsorted_list[left] > unsorted_list[high]:
            unsorted_list[left], unsorted_list[high] = unsorted_list[high], unsorted_list[left]
        return left

    if low < high:
        pivot = partition(low, high)
        quick_sort(unsorted_list, low, pivot-1)
        quick_sort(unsorted_list, pivot+1, high)


if __name__ == "__main__":
    # unsorted_list = [5, 9, 3, 1, 2, 8, 4, 7, 6]
    # bubble_sort(unsorted_list)

    # unsorted_list = [5, 9, 3, 1, 2, 8, 4, 7, 6, 10]
    # sorted_list = merge_sort(unsorted_list)
    # print(sorted_list)

    unsorted_list = [12, 7, 10, 5, 2, 4, 9, 8, 6, 3, 1, 0, 8, 5]
    quick_sort(unsorted_list, 0, len(unsorted_list)-1)
    print(unsorted_list)