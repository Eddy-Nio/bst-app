from .nodes import BSTNode, WordNode

class BinarySearchTree:
    """
    A class representing a Binary Search Tree (BST).
    The BinarySearchTree class provides methods to insert values into the tree and 
    perform a reverse in-order traversal to retrieve values in descending order.
    Attributes:
        root (BSTNode): The root node of the binary search tree.
        Initializes an empty Binary Search Tree (BST).
        The root of the tree is set to None, indicating that the tree is initially empty.
    """
    
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        """
        Inserts a numeric value into the Binary Search Tree (BST).

        This method adds a new node with the specified integer value into the BST.
        If the tree is empty, the new node becomes the root. Otherwise, the method
        calls a helper function to recursively find the correct position for the new node.

        Args:
            value (int): The integer value to be inserted into the BST.

        Returns:
            None
        """
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(value, self.root)

    def _insert_recursive(self, value: int, current_node: BSTNode) -> None:
        """
        Recursively inserts a value into the binary search tree (BST).

        Args:
            value (int): The value to be inserted into the BST.
            current_node (BSTNode): The current node in the BST where the value is being compared.

        Returns:
            None

        This method compares the given value with the value of the current node:
            - If the value is less than the current node's value, it proceeds to the left subtree.
            - If the value is greater than the current node's value, it proceeds to the right subtree.
            - If the appropriate child node (left or right) is None, it creates a new BSTNode with the given value.
            - Otherwise, it continues the recursion with the appropriate child node.
        """
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = BSTNode(value)
            else:
                self._insert_recursive(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = BSTNode(value)
            else:
                self._insert_recursive(value, current_node.right)

    def reverse_in_order(self) -> list[int]:
        """
        Perform a reverse in-order traversal of the binary search tree and return 
        the values in descending order.

        This method traverses the tree starting from the rightmost node, then visits 
        the root, and finally the leftmost node, ensuring that the values are collected 
        in descending order.

        Returns:
            list[int]: A list of integers representing the values of the tree in 
            descending order.
        """
        result = []
        self._reverse_in_order_recursive(self.root, result)
        return result

    def _reverse_in_order_recursive(self, node: BSTNode, result: list) -> None:
        """
        Perform a reverse in-order traversal of the binary search tree (BST) recursively.

        This helper method traverses the BST in reverse in-order (right, root, left) and appends 
        the value of each visited node to the provided result list.

        Args:
            node (BSTNode): The current node in the BST.
            result (list): The list to which node values are appended during traversal.

        Returns:
            None
        """
        if node:
            self._reverse_in_order_recursive(node.right, result)
            result.append(node.value)
            self._reverse_in_order_recursive(node.left, result)


class WordFrequencyBST:
    """
    A Binary Search Tree (BST) implementation for tracking word frequencies.
    
    This class allows for the insertion of words into the BST, where each node
    contains a word and its frequency count. It supports updating the frequency
    count if a word already exists in the tree and provides an in-order traversal
    method to retrieve the words and their counts in alphabetical order.
    """
   
    def __init__(self):
        self.root = None

    def insert(self, word: str) -> None:
        """
        Inserts or updates a word in the Binary Search Tree (BST).

        If the tree is empty, the word will be inserted as the root node.
        If the tree is not empty, the word will be inserted in its correct 
        position according to BST properties.

        Args:
            word (str): The word to be inserted or updated in the BST.

        Returns:
            None
        """
        if self.root is None:
            self.root = WordNode(word)
        else:
            self._insert_recursive(word, self.root)

    def _insert_recursive(self, word: str, current_node: WordNode) -> None:
        """
        Recursively inserts a word into the binary search tree, updating the count if the word already exists.

        Args:
            word (str): The word to be inserted into the tree.
            current_node (WordNode): The current node in the tree being compared.

        Returns:
            None

        Raises:
            TypeError: If the word is not a string or current_node is not a WordNode.

        The method compares the word to be inserted with the word in the current node:
            - If the word is less than the current node's word, it moves to the left child.
            - If the word is greater than the current node's word, it moves to the right child.
            - If the word is equal to the current node's word, it increments the count of the current node.
        """
        if word < current_node.word:
            if current_node.left is None:
                current_node.left = WordNode(word)
            else:
                self._insert_recursive(word, current_node.left)
        elif word > current_node.word:
            if current_node.right is None:
                current_node.right = WordNode(word)
            else:
                self._insert_recursive(word, current_node.right)
        else:
            current_node.count += 1

    def in_order_traversal(self) -> list[tuple]:
        """
        Perform an in-order traversal of the binary search tree.

        This method traverses the tree in in-order fashion (left, root, right)
        and collects all the nodes in a list of tuples. Each tuple contains a word
        and its corresponding count, sorted in alphabetical order.

        Returns:
            list[tuple]: A list of tuples where each tuple consists of a word (str)
                         and its count (int), sorted in alphabetical order.
        """
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node: WordNode, result: list) -> None:
        """
        Perform an in-order traversal of the binary search tree recursively.

        This helper method traverses the tree in in-order fashion (left subtree, 
        root node, right subtree) and appends each node's word and count to the 
        result list.

        Args:
            node (WordNode): The current node in the binary search tree.
            result (list): The list that accumulates the (word, count) tuples 
                           from the nodes during traversal.

        Returns:
            None
        """
        if node:
            self._in_order_recursive(node.left, result)
            result.append((node.word, node.count))
            self._in_order_recursive(node.right, result)