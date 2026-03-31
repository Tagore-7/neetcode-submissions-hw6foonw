class TreeNode:
    def __init__(self,key, val, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)

        if not self.root:
            self.root = newNode
            return 
        
        current = self.root
        while True:
            if  key < current.key:
                if not current.left:
                    current.left = newNode
                    return
                current = current.left 
            elif key > current.key:
                if not current.right:
                    current.right = newNode
                    return 
                current = current.right
            else:
                current.val = val 
                return 

    def get(self, key: int) -> int:
        current = self.root 
        while current:
            if  key < current.key:
                current = current.left
            elif  key > current.key:
                current = current.right
            else:
                return current.val
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1 
        current = self.root
        while current.left:
            current =  current.left 
        return current.val 

    def getMax(self) -> int:
        if not self.root:
            return -1 
        current = self.root
        while current.right:
            current =  current.right 
        return current.val

    def remove(self, key: int) -> None:
        self.root = self.removehelper(self.root, key)

    def removehelper(self, root, key):
        if not root:
            return None

        if key < root.key:
            root.left = self.removehelper(root.left, key)
        elif key > root.key:
            root.right = self.removehelper(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.findMin(root.right)
                root.val = minNode.val
                root.key = minNode.key
                root.right = self.removehelper(root.right, minNode.key)
        return root 
    
    def findMin(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr 


    def getInorderKeys(self) -> List[int]:
        values = []
        
        def helper(root, values):
            if not root:
                return 
            helper(root.left, values)
            values.append(root.key)
            helper(root.right, values)

        helper(self.root, values )

        return values 
            
