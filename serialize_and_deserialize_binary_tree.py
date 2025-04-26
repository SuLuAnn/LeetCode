class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return 'N'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)
        

    def deserialize(self, data):
        res = [0]
        data = data.split(',')
        def preorder():
            if data[res[0]] is 'N':
                res[0] += 1
                return None
            root = TreeNode(int(data[res[0]]))
            res[0] += 1
            root.left = preorder()
            root.right = preorder()
            return root

        return preorder()