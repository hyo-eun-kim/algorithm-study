'''
복습문제1번 : 완주하지 못한 선수
https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3'''

# "hash"라는 주제가 있었기 때문에 쉽게 풀 수 있었다
def solution(participant, completion):
    from collections import defaultdict
    dict = defaultdict(int)
    for name in participant:
        dict[name] += 1

    for name in completion:
        dict[name] -= 1

    for name, count in dict.items():
        if count == 1:
            return name

if __name__ == "__main__":
    print(solution(["leo", "kiki", "eden"],
                   ["eden", "kiki"]))

    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
                   ["josipa", "filipa", "marina", "nikola"]))

    print(solution(["mislav", "stanko", "mislav", "ana"],
                   ["stanko", "ana", "mislav"]))