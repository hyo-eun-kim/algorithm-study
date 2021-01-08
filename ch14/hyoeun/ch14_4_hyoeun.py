'''
https://leetcode.com/problems/invert-binary-tree/
이진 트리 반전
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

'''
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 나의 풀이
# 60ms (faster than 5%)
# 오 이 풀이가 DFS로 풀어낸 풀이.. !
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def recursive(node: TreeNode):
            if node:
                node.right, node.left = node.left, node.right
                recursive(node.right)
                recursive(node.left)
        recursive(root)
        return root


# 책 풀이1
class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root

# 책 풀이2 (BFS)
class Solution3:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print(root.left.val, root.right.val)
    print(root.left.left.val, root.left.right.val, root.right.left.val, root.right.right.val)

    solution = Solution()
    solution.invertTree(root)

    print(root.left.val, root.right.val)
    print(root.left.left.val, root.left.right.val, root.right.left.val, root.right.right.val)

    # root2 = TreeNode(4)
    # root2.left = TreeNode(2)
    # root2.right = TreeNode(7)
    #
    # #print(root2.val)
    # print(root2.val, root2.left.val, root2.right.val)
    #
    # root2.right, root2.left = root2.left, root2.right
    # print(root2.val, root2.left.val, root2.right.val)