class TrieNode:
    def __init__(self):
        """
        initializing a node of trie
        isEndOfWord flag used for the leaf nodes
        """
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        """
        initializing the trie data structure with a root node
        """
        self.root = self.getNode()

    def getNode(self):
        """
        Create a node in the memory
        :return: a new node with children and isEOW flag
        """
        return TrieNode()

    def charToIndex(self, ch):
        """
        converts characters to index starting from 0
        :param ch: any english albhabet
        :return: ascii value
        """
        return ord(ch) - ord('a')

    def insert(self, key):
        """
        function for inserting words into prefix tree (trie)
        :param value: word string to be inserted
        """
        rootNode = self.root
        length = len(key)
        for lev in range(length):
            index = self.charToIndex(key[lev])
            if index not in rootNode.children:
                rootNode.children[index] = self.getNode()
            rootNode = rootNode.children[index]
        rootNode.isEndOfWord = True


if __name__ == '__main__':
    t = Trie()

    keys = ['there', 'the', 'them', 'therefore']
    for key in keys:
        t.insert(key)
