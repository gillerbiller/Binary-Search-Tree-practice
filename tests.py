import unittest
import BST1

class Test_binary_search_tree(unittest.TestCase):

    def test_add_node(self):

        root = binary_search_tree(15)
        root.add_node(10)
        root.add_node(5)
        root.add_node(1)
        root.add_node(14)
        root.add_node(12)
        root.add_node(20)
        root.add_node(16)
        root.add_node(16)
        root.add_node(18)
        root.add_node(23)
        root.add_node(24)
        root.add_node(35)

        root.add_node(14)
        self.assertTrue(root.left.right.right.value == 14)


    def test_delete_node(self):
        root = binary_search_tree(15)
        root.add_node(10)
        root.add_node(5)
        root.add_node(1)
        root.add_node(14)
        root.add_node(12)
        root.add_node(20)
        root.add_node(16)
        root.add_node(16)
        root.add_node(18)
        root.add_node(23)
        root.add_node(24)
        root.add_node(35)

        root.test_delete_node(1)
        self.assertTrue(root.left.left.left.value == None)

    def test_get_min_value(self):

    def test_search_tree_for_value(self):

if __name__ == '__main__':
    unittest.main()

