class Node:
    def __init__(self, key,
                 value=None, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

class BST:
    def __init__(self, key = None, value = None):
        if key == None:
            self.root = None
        else:
            self.root = Node(key, value)

    def search(self, key, ref=None):
        if self.root is None:
            return None
      
        if ref is None:
            ref = self.root

        if key == ref.key:
            return ref
        
        elif key < ref.key and ref.left is None:
            return None
        
        elif key < ref.key:
            return self.search(key, ref.left)
        
        elif key > ref.key and ref.right is None:
            return None
        
        else:
            return self.search(key, ref.right)      
        

    def insert(self, key, value=None, root=None):

        node = Node(key, value)

        if self.root is None:
            self.root = node
            return

        if root is None:
            root = self.root

        if node.key <= root.key and root.left is None:
            root.left = node
            node.parent    = root
            return

        elif node.key <= root.key:
            root = root.left
            return self.insert(key, value=None, root=root)

        elif node.key > root.key and root.right is None:
            root.right = node
            node.parent     = root
            return

        else:
            root = root.right
            return self.insert(key, value=None, root=root)
        
    def delete(self, key):
        to_delete = self.search(key)
        if to_delete is None:
            return  # Schlüssel nicht gefunden

        parent = to_delete.parent

        ## Node is leaf
        if to_delete.left is None and to_delete.right is None:
            if to_delete == self.root:
                self.root = None
            elif key < parent.key:
                parent.left = None
            else:
                parent.right = None
            return
        
        ## Node has one child
        if to_delete.left is None:
            if to_delete == self.root:
                self.root = to_delete.right
                self.root.parent = None
            else:
                if key < parent.key:
                    parent.left = to_delete.right
                else:
                    parent.right = to_delete.right
                to_delete.right.parent = parent
            return
        
        elif to_delete.right is None:
            if to_delete == self.root:
                self.root = to_delete.left
                self.root.parent = None
            else:
                if key < parent.key:
                    parent.left = to_delete.left
                else:
                    parent.right = to_delete.left
                to_delete.left.parent = parent
            return
        
        ## Node has two children
        else:
            successor = self.get_min(to_delete.right)
            to_delete.key = successor.key
            to_delete.value = successor.value
            if successor.key < successor.parent.key:
                successor.parent.left = None
            else:
                successor.parent.right = None
            
    def get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    # Durch perplexity.ai erzeugter Code um den Baum als
    # ASCI-Art auszugeben
    def to_ascii(self):
        if self.root is None:
            return ""
        return self._to_ascii(self.root, "", True, "")

    def _to_ascii(self, node, prefix, is_tail, result):
        if node.right is not None:
            new_prefix = prefix + ("│   " if is_tail else "    ")
            result = self._to_ascii(node.right, new_prefix, False, result)
        result += prefix + ("└── " if is_tail else "┌── ") + str(node.key) + "\n"
        if node.left is not None:
            new_prefix = prefix + ("    " if is_tail else "│   ")
            result = self._to_ascii(node.left, new_prefix, True, result)
        return result