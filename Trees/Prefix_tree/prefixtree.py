#!python3
# https://www.geeksforgeeks.org/trie-insert-and-search/

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        # TODO
        if self.root.num_children() == 0:
            return True
        else:
            return False

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        # TODO
        active_node = self.root

        for char in string:
            # print(char)
            if not active_node.has_child(char):
                return False
            active_node = active_node.get_child(char)
        if active_node.is_terminal():
            return True
        else:
            return False

    def insert(self, string):
        """Insert the given string into this prefix tree."""
        # TODO
        #if current does not have children:
            #insert new node with current #char in string
            #create a new node
            #add it as a child of current node
          #if there is a child the child is the letter of the string
          #current = that child
        #when I'm at the end of the string I want to make the last character terminal

        current = self.root
        #"h e l l o"
        for char in string:
            # print(char)
            if not current.has_child(char):
                current.add_child(char, PrefixTreeNode(char))
                # print("Current", current)
            current = current.get_child(char)
            # print("Change to next")
        # print("End", current)
        if not current.is_terminal():
            self.size += 1
            current.terminal = True

    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node."""
        # Match the empty string
        if len(string) == 0:
            return self.root, 0
        # Start with the root node
        node = self.root
        depth = 0
        # TODO

        for letter in string:
            if node.has_child(letter):
                node = node.get_child(letter)
                depth += 1
            else:
                return None, 0

        return node, depth

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        completions = []
        # TODO

        #get that node object using find prefix node
        node = self._find_node(prefix)[0]
        # print(node)

        if node == None:
            return completions

        # If terminal, append to completeion list
        if node.is_terminal():
            completions.append(prefix)

         # If not then traverse
        if node.num_children() > 0:
            # for every child of this node
            for child in node.children:
                # Get child node of this node
                # Use traverse on node
                self._traverse(child, prefix + child.character, completions.append)

        return completions

        '''
        Go through each child of the root node
            SHould the prefix passed in match them
                Go down each branch until a terminal node is hit, add that to list
            >>
        '''

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        all_strings = []
        # TODO

        node = self.root
        if node.num_children() > 0:
            # we need to loop the children
            for child in node.children:
                # call traverse on all children
                self._traverse(child,child.character, all_strings.append)
        

        return all_strings
        '''
        Go though all children of the root
            Go through the branches of each
                for each terminal node, add the word
        '''

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""
        # TODO
        #If node is termminal
        if node.is_terminal():
            visit(prefix)
        #If node has children (can be terminal and have children)    
        if node.num_children() > 0:
            # we need to loop the children
            for child in node.children:
                # call traverse on all children
                self._traverse(child,prefix+child.character, visit)


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


def main():
    # Simpe test case of string with partial substring overlaps
    strings = ['ABC', 'ABD', 'A', 'XYZ']
    create_prefix_tree(strings)

    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
        if len(tongue_twisters) > 1:
            print('\n' + '='*80 + '\n')


if __name__ == '__main__':
    main()

