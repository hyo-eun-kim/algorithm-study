"""
## 14-6. 이진 트리 직렬화 & 역직렬화

이진 트리를 배열로 직렬화하고, 반대로 역직렬화하는 기능을 구현하라.
즉 다음과 같은 트리는 [1, 2, 3, null, null, 4, 5] 형태로 직렬화할 수 있을 것이다.
   1
 /  \
2    3
    / \
  4    5
"""
from typing import *
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # 112ms
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()
            if node:
                queue.extend([node.left, node.right])
                result.append(str(node.val))
            else:
                result.append('#')

        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "#":
            return None

        nodes = deque(data.split())

        root = TreeNode(int(nodes.popleft()))
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                l, r = nodes.popleft(), nodes.popleft()
                node.left = TreeNode(int(l)) if l != '#' else None
                node.right = TreeNode(int(r)) if r != '#' else None
                queue.extend([node.left, node.right])

        return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    ser = Codec()
    deser = Codec()
    print(ser.serialize(root))
    print(deser.deserialize(ser.serialize(root)))