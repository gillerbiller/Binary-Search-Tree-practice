class binary_search_tree:
    """Return a binary search tree"""
    def __init__(self, value):
        self.value = value
        self.right = right
        self.left = left

    def add_node(self, value):
        """Insert a node with value to binary search tree"""
        current_node = self

        while True:

            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = binary_search_tree(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = binary_search_tree(value)
                    break
                else:
                    current_node = current_node.right
        return self

    def delete_node(self, value, parent_node = None):
        """Remove a node with value from binary search tree"""
        current_node = self

        while current_node is not None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.get_min_value()
                    current_node.right.delete_node(current_node.value, current_node)
                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else: 
                        pass #single-node tree, no action required 
                elif parent_node.left == current_node:
                    parent_node.left = current_node.left if current_node.left \
                    is not None else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left \
                    is not None else current_node.right
                break
        return self

    def get_min_value(self):
        """Return node with minimum value from binary search tree"""
        current_node = self

        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def search_tree_for_value(self, value):
        """Return true if value in binary search tree else return false"""
        current_node = self 

        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False




                            