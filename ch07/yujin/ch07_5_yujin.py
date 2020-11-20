class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        투 포인터를 한 번에 두는 게 아니라 두 번으로 나누는 것
        --> 하나의 loop 안에서 해결할 수가 없음. 이렇게 되면 nested loop 구조가 될 수 밖에 없으므로
        한 번 쫙 돌고, 반대 방향으로 한 번 쭉 도는 형식으로 가야됨.
        """

        out = [1 for i in range(len(nums))]
        p = 1
        for i in range(len(nums)):
            out[i] = p
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1): # backstep
            out[i] *= p
            p *= nums[i]

        return out
