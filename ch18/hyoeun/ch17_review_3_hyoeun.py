'''
https://programmers.co.kr/learn/courses/30/lessons/42746#
이전에 풀었던 문제입니다 :)
'''
def solution(numbers):
    def merge(left, right):
        l_index, r_index = 0, 0
        merge_numbers = []
        while l_index != len(left) and r_index != len(right):
            l_r = str(left[l_index]) + str(right[r_index])
            r_l = str(right[r_index]) + str(left[l_index])
            if l_r >= r_l:
                merge_numbers.append(left[l_index])
                l_index += 1
            else:
                merge_numbers.append(right[r_index])
                r_index += 1
        while l_index != len(left):
            merge_numbers.append(left[l_index])
            l_index += 1
        while r_index != len(right):
            merge_numbers.append(right[r_index])
            r_index += 1

        return merge_numbers

    def split(numbers):
        if len(numbers) <= 1:
            return numbers
        else:
            mid = len(numbers) // 2
            left = split(numbers[:mid])
            right = split(numbers[mid:])
            return merge(left, right)

    numbers = split(numbers)
    answer = ''.join(list(map(str, numbers)))
    if answer.rstrip('0') == '':
        return "0"
    return answer