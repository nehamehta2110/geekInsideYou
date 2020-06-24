class TrieNode:
    def __init__(self):
        """
        initializing a node of trie
        isEOW is isEndOfWord flag used for the leaf nodes
        """
        self.children = [None] * 26
        self.isEOW = False


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

    def insert(self, value):
        """
        function for inserting words into prefix tree (trie)
        :param value: word string to be inserted
        """
        rootNode = self.root
        length = len(value)

        for step_size in range(length):
            index = self.charToIndex(value[step_size])

            if not rootNode.children[index]:
                rootNode.children[index] = self.getNode()
            rootNode = rootNode.children[index]

        rootNode.isEOW = True

    def search(self, word):
        """
        utility function that searches for a word in trie
        :param word: search word
        :return: boolean, if true, word is present otherwise not
        """
        rootNode = self.root
        length = len(word)

        for _ in range(length):
            index = self.charToIndex(word[_])

            if not rootNode.children[index]:
                return False

            rootNode = rootNode.children[index]
        return rootNode is not None and rootNode.isEOW

    def delete(self, word):
        """
        utility function that deletes a word in trie
        :param word: word to be deleted
        """
        rootNode = self.root
        length = len(word)

        for _ in range(length):
            index = self.charToIndex(word[_])

            if not rootNode.children[index]:
                return 'word not found'

            rootNode = rootNode.children[index]
        if not rootNode:
            return 'word not found'
        else:
            rootNode.isEOW = False
            return 'word deleted'


if __name__ == '__main__':
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

        # Search for different keys
    if t.search('the'):
        print('present')
    else:
        print('not present')

    print(t.delete('the'))
    if t.search('the'):
        print('present')
    else:
        print('not present')
