class BSTNode:
    """Node for Binary Search Tree (Problem 1)."""
    
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class WordNode:
    """Node for Word Frequency BST (Problem 2)."""
    
    def __init__(self, word: str):
        self.word = word
        self.count = 1
        self.left = None
        self.right = None