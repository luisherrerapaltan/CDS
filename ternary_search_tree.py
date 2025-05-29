# Represents a single node in the Ternary Search Tree
class Node:
    def __init__(self, char):
        self.char = char             # Character stored in this node
        self.terminates = False      # Indicates if a word ends at this node
        self.left = None             # Left child (chars < self.char)
        self.eq = None               # Middle child (next character in word)
        self.right = None            # Right child (chars > self.char)


    def __str__(self, indent="") -> str:
        lines = [f"{indent}char: {self.char}, terminates: {self.terminates}"]
        return "\n".join(lines)


# Implements the Ternary Search Tree data structure
class TernarySearchTree:
    def __init__(self):
        self.root = None              # Root of the tree
        self._size = 0                # Number of unique words in the tree
        self._empty_string = False    # Tracks whether the empty string "" is stored

    # Inserts a word into the tree
    def insert(self, word):
        pass
