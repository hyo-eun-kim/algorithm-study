'''
47. 이진 트리 직렬화 & 역직렬화

이진 트리를 배열로 직렬화하고, 반대로 역직렬화하는 기능을 구현하라. 즉 다음과 같은 트리는 
[1,2,3,null,null,4,5] 형태로 직렬화할 수 있을 것이다.

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root: 
            return '#'
        val = str(root.val)
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        # print(','.join([val, left, right]))

        return ' '.join([val, left, right])

    def deserialize(self, data):
        self.data = data
        if self.data[0] == '#': return None
        node = TreeNode(self.data[:self.data.find(' ')]) 
        node.left = self.deserialize(self.data[self.data.find(' ')+1:])
        node.right = self.deserialize(self.data[self.data.find(' ')+1:])
        return node
    
    # 140 ms

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
    