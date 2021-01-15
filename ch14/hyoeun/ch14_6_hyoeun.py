'''
47. 이진 트리 직렬화 & 역직렬화
이진트리를 배열로 직렬화하고, 반대로 역직렬화하는 기능을 구현하라.
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
'''
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        queue = deque()
        queue.append(root)
        answer = [-1]
        while queue:
            node = queue.popleft()
            if not node:
                answer.append(None)
            else:
                answer.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        while answer[-1] is None:
            answer.pop()
        return answer

    def deserialize(self, data):
        if len(data) == 1:
            return None

        data = deque(data[1:])
        root = TreeNode(data.popleft())
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node and data:
                left = data.popleft()
                node.left = TreeNode(left) if left is not None else None
                queue.append(node.left)
            if node and data:
                right = data.popleft()
                node.right = TreeNode(right) if right is not None else None
                queue.append(node.right)
        return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(7)

    ser = Codec()
    deser = Codec()

    print(ser.serialize(root))
    print(deser.deserialize(ser.serialize(root)))