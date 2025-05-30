# Represents a single node in the Ternary Search Tree
class Node:
    def __init__(self, char):
        self.char = char             # Character stored in this node
        self.terminates = False      # Indicates if a word ends at this node
        self.left = None             # Left child (chars < self.char)
        self.eq = None               # Middle child (next character in word)
        self.right = None            # Right child (chars > self.char)

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
                node = Node(char) # Create a node if missing

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

    # Searches for a word or prefix in the tree
    # exact = True → look for full word
    # exact = False → allow prefix matches
    def search(self, word, exact=False):
        if word == "":
            # For empty string, return True if it was explicitly added
            return True if not exact else self._empty_string

        # Internal recursive function to traverse the tree
        def _search(node, word, i):
            if not node:
                return False  # Dead end: word not found

            char = word[i]
            if char < node.char:
                return _search(node.left, word, i)
            elif char > node.char:
                return _search(node.right, word, i)
            else:
                if i + 1 == len(word):
                    # At final character
                    return node.terminates if exact else True
                return _search(node.eq, word, i + 1)

        return _search(self.root, word, 0)

    # Returns the number of unique words stored in the tree
    def __len__(self):
        return self._size

    # Returns all stored words in the tree as a list
    def all_strings(self):
        words = []
        if self._empty_string:
            words.append("")  # Include empty string if present

        # Internal recursive function to collect words from the tree
        def _collect(node, prefix):
            if not node:
                return
            _collect(node.left, prefix)                   # Visit left subtree
            if node.terminates:
                words.append(prefix + node.char)          # Add complete word
            _collect(node.eq, prefix + node.char)         # Visit middle (next char)
            _collect(node.right, prefix)                  # Visit right subtree

        _collect(self.root, "")
        return words

    # Returns a string representation of the entire tree
    def __str__(self):
        if not self.root:
            return f"terminates: {self._empty_string}"
        return f"terminates: {self._empty_string}\n" + self.root.__str__("  ")
