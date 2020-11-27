class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        # counter: 각 글자 별 등장횟수
        # seen: 이미 등장한 글자
        # stack: 최종 결과를 담을 stack
        for char in s:
            counter[char] -= 1 # 등장횟수를 1로 하나 줄임 (한 번 탐색했으므로)
            if char in seen: # 이미 등장한 글자면 continue
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                # 반복조건:
                # stack이 empty일 때까지
                # stack의 top이 char보다 사전순서가 앞일 때까지
                # stack의 top에 해당하는 글자가 문자열 내에서 모두 탐색될 때까지
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return "".join(stack)
