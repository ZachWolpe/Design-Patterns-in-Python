class Node:
    def __init__(self, value, left=None, right=None):
        self.right  = right
        self.left   = left
        self.value  = value
        self.parent = None

        # update parent of children nodes.
        if left:
            self.left.parent = self
        if right:
            self.right.parent = self
    
    def __iter__(self):
        """Exposes the Iterator interface to the client."""
        return InOrderIterator(self)
    

class InOrderIterator:
    def __init__(self, root):
        self.root = self.current = root
        self.yielded_start = False
        while self.current.left:
            # bottom left node
            self.current = self.current.left
    
    def __next__(self):
        """Returns the next node in the tree: InOrder traversal."""
        if not self.yielded_start:
            # first node (bottom left)
            self.yielded_start = True
            return self.current
        
        if self.current.right:
            # node right of current exists
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            p = self.current.parent
            while p and self.current == p.right:
                # node right of current node (right of parent)
                self.current = p
                p = p.parent
            self.current = p
            if self.current:
                return self.current
            else:
                raise StopIteration


# Recursive solution -----------------------------++
def traverse_in_order(root):
    def traverse(current):
        if current.left:
            for left in traverse(current.left):
                yield left
        yield current
        if current.right:
            for right in traverse(current.right):
                yield right
    
    for node in traverse(root):
        yield node
# Recursive solution -----------------------------++

    

if __name__ == '__main__':
    #     1
    #    / \
    #   2   3
    
    # in-order:     213
    # pre-order:    123
    # post-order:   231
    root = Node(1,
                Node(2),
                Node(3))
    it = iter(root)
    print([next(it).value for _ in range(3)])

    for x in root:
        print(x.value)
    
    # recursive solution -----------------------------++
    for y in traverse_in_order(root):
        print(y.value)
    # recursive solution -----------------------------++
