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

    # Recursively builds a string representation of the subtree rooted at this node
    def __str__(self, indent="") -> str:
        lines = [f"{indent}char: {self.char}, terminates: {self.terminates}"]
        if self.left:
            lines.append(f"{indent}_lt: " + self.left.__str__(indent + "  "))
        if self.eq:
            lines.append(f"{indent}_eq: " + self.eq.__str__(indent + "  "))
        if self.right:
            lines.append(f"{indent}_gt: " + self.right.__str__(indent + "  "))
        return "\n".join(lines)

# Implements the Ternary Search Tree data structure
class TernarySearchTree:
    def __init__(self):
        self.root = None              # Root of the tree
        self._size = 0                # Number of unique words in the tree
        self._empty_string = False    # Tracks whether the empty string "" is stored

    # Inserts a word into the tree
    def insert(self, word):
        if word == "":
            # Special handling for empty string (not stored in the tree structure)
            if not self._empty_string:
                self._empty_string = True
                self._size += 1
            return

        # Internal recursive function to insert characters into the tree
        def _insert(node, word, i):
            char = word[i]
            if not node:
                node = Node(char)  # Create a node if missing

            if char < node.char:
                node.left = _insert(node.left, word, i)
            elif char > node.char:
                node.right = _insert(node.right, word, i)
            else:
                # Matching character: move to middle child (eq)
                if i + 1 == len(word):
                    # Reached last character of word
                    if not node.terminates:
                        node.terminates = True
                        self._size += 1
                else:
                    node.eq = _insert(node.eq, word, i + 1)
            return node

        # Start the recursive insertion at the root
        self.root = _insert(self.root, word, 0)
