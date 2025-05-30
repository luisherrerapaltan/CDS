import random
import time

start_script_time = time.time()

############################## CLASS DEFINITION ###############################
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

############################## PERFORMANCE TEST ##############################
with open('data/corncob_lowercase.txt') as file:
    words = [line.strip() for line in file]

sizes = [100, 500, 1_000, 5_000, 10_000, 20_000, 30_000, 40_000, 50_000]

samples = [random.sample(words, k=size) for size in sizes]

# Time to insert 20 non-existing words in trees of different sizes
nr_runs = 20
times_insert = {}
for sample in samples:
    tst = TernarySearchTree()
    insert_sample = random.sample([w for w in words if w not in sample], k=20)
    for word in sample:
        tst.insert(word)
    times_insert[len(sample)] = 0.0
    for _ in range(nr_runs):
        start_time = int(time.time() * 1e9)
        for word in insert_sample:
            tst.insert(word)
        end_time = int(time.time() * 1e9)
        times_insert[len(sample)] += end_time - start_time
    times_insert[len(sample)] /= nr_runs*1_000_000.0

#Times of searching 10 existing and 10 non existing words in trees of different sizes
nr_runs = 20
times_search = {}
for sample in samples:
    tst = TernarySearchTree()
    existing = random.sample(sample, k=10)
    non_existing = random.sample([w for w in words if w not in sample], k=10)
    search_sample = existing + non_existing
    for word in sample:
        tst.insert(word)
    times_search[len(sample)] = 0.0
    for _ in range(nr_runs):
        start_time = int(time.time() * 1e9)
        for word in search_sample:
            tst.search(word)
        end_time = int(time.time() * 1e9)
        times_search[len(sample)] += end_time - start_time
    times_search[len(sample)] /= nr_runs*1_000_000.0

end_script_time = time.time()

# Save timing info
with open("timings.txt", "w") as f:
    f.write(f"- script execution: {end_script_time - start_script_time:.6f} seconds\n")

    f.write("- tst.insert():\n")
    for size, duration in times_insert.items():
        f.write(f"  size={size}: {duration:.6f} ms\n")

    f.write("- tst.search():\n")
    for size, duration in times_search.items():
        f.write(f"  size={size}: {duration:.6f} ms\n")
