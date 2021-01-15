'''
46. 두 이진 트리 병합
두 이진 트리를 병합하라. 중복되는 노드는 값을 합산한다.
https://leetcode.com/problems/merge-two-binary-trees/
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 88ms faster than 70%
# 15.7MB less than 30%
# 오와 ... 닮고싶은 코드 ....
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            # t1이 없다면 + t2이 없다면 / t1이 없다면 + t2가 있다면
            return t2
        elif not t2:
            # t1이 있고 t2가 없다면
            return t1
        else:
            # t1도 있고 t2도 있다면
            res = TreeNode(t1.val + t2.val)
            res.left = self.mergeTrees(t1.left, t2.left)
            res.right = self.mergeTrees(t1.right, t2.right)
        return res


# 나의 코드 부끄럽다 ...
# 104 (faster than 14%)
# 16 MB (less than 16%)
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def merge(t: TreeNode, t1: TreeNode, t2: TreeNode):
            if t1 and t2:
                t.val = t1.val + t2.val
            elif t1:
                t.val = t1.val  # t1 not None, t2 None
            elif t2:
                t.val = t2.val  # t1 None, t2 not None
            else:
                return  # t1, t2 None

            if (t2 and t2.left) or (t1 and t1.left):
                t.left = TreeNode()
                t1_left = None if t1 is None else t1.left
                t2_left = None if t2 is None else t2.left
                merge(t.left, t1_left, t2_left)
            if (t2 and t2.right) or (t1 and t1.right):
                t.right = TreeNode()
                t1_right = None if t1 is None else t1.right
                t2_right = None if t2 is None else t2.right
                merge(t.right, t1_right, t2_right)

        if not t1 and not t2:
            return None
        t = TreeNode()
        merge(t, t1, t2)
        return t

