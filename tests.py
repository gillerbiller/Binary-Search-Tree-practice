import unittest
import BST1

class Test_binary_search_tree(unittest.TestCase):

    def test_number_one(self):

        root = binary_search_tree(15)
        root.left = binary_search_tree(10)
        root.left.left = binary_search_tree(5)
        root.left.right = binary_search_tree(14)
        root.left.left.left = binary_search_tree(1)
        root.left.left.right = binary_search_tree(5)
        root.left.right.left = binary_search_tree(12)
        root.right = binary_search_tree(20)
        root.right.left = binary_search_tree(16)
        root.right.right = binary_search_tree(24)
        root.right.left.left = binary_search_tree(16)
        root.right.left.right = binary_search_tree(18)
        root.right.right.left = binary_search_tree(23)
        root.right.right.right = binary_search_tree(35)

        root.add_node(14)
        self.assertTrue(root.left.right.right.value == 14)

        root.delete_node


    def test_delete_node(self):

    def test_get_min_value(self):

    def test_search_tree_for_value(self):

if __name__ == '__main__':
    unittest.main()

