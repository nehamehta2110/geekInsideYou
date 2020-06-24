class TrieNode:

    def __init__(self):
        """
        initializing a node of trie
        isEOW is isEndOfWord flag used for the leaf nodes
        """
        self.children = {}
        self.isEOW = False


class Trie:
    def __init__(self):
        """
        initializing the trie data structure with a root node
        """
        self.root = self.getNode()
        self.suggestList = []  # list of suggested words by auto completion

    def getNode(self):
        """
        Create a node in the memory
        :return: a new node with children and isEOW flag
        """
        return TrieNode()

    def insert(self, value):
        """
        function for inserting words into prefix tree (trie)
        :param value: word string to be inserted
        """
        rootNode = self.root

        for step in list(value):  # inserting each character of the word
            if not rootNode.children.get(step):  # check if character is not already present
                rootNode.children[step] = self.getNode()
            rootNode = rootNode.children[step]

        rootNode.isEOW = True  # set end of word flag to true when the word is inserted

    def search(self, word):
        """
        utility function that searches for a word in trie
        :param word: search word
        :return: boolean, if true, word is present otherwise not
        """
        rootNode = self.root

        for i in list(word):

            if not rootNode.children[i]:
                return False

            rootNode = rootNode.children[i]
        return rootNode is not None and rootNode.isEOW
        # if all characters of a word are present in children nodes of
        # rootnode i.e. updated rootNode is not none and end of word flag is true,
        # then, the word is present. .

    def suggestion(self, rootNode, temp_word):
        """
        recursive function to suggest words
        :return suggestion list with all possible suggestions

        """
        if rootNode.isEOW:
            self.suggestList.append(temp_word)
        for alpha, node in rootNode.children.items():
            self.suggestion(node, temp_word + alpha)

    def autoCompleter(self, word):
        """
        function for auto completion
        """

        rootNode = self.root
        not_present = False  # not present flag set to false initially
        temp_word = ""

        for a in list(word):
            if not rootNode.children.get(a):
                not_present = True  # set True if any char of search word not present
                break
            temp_word += a
            rootNode = rootNode.children[a]

        if not_present:
            print('word not in dictionary')
            return False
        elif rootNode.isEOW and not rootNode.children:
            print('no suggestion for the query')
            return False
        self.suggestion(rootNode, temp_word)  # calling suggestion function with temporary prefix

        for s in self.suggestList:
            print(s)
        # print suggestions


if __name__ == '__main__':
    keys = ["fable", "false", "hi", "hello", "bye",
            "better", "fabulous", "hence", "home", "them", "there", "therefore"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    search_list = ['t', 'th', 'the', 'ho', 'home']
    for search_key in search_list:
        if t.search(search_key):
            print('Yay! The key "{}" is present'.format(search_key))
        else:
            print('No! The key "{}" is not present'.format(search_key))

    suggest_query = ['fa', 'fabl']
    for suggest_key in suggest_query:
        print("the suggestions for word " + suggest_key + ":")
        t.autoCompleter(suggest_key)
