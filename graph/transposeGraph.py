class adj_node:
    """
    implementation for adjacency list
    """

    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    """"
    class implementation of graph edges and vertices
    """

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_node_edge(self, src, dest):

        """
        adds edge bwtween 2 vertices in an undirected graph
        """
        node = adj_node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def display_graph(self):

        """
        displays adjacency list for each element
        """

        for i in range(self.V):

            print("Ajacency list of element {}".format(i))

            temp = self.graph[i]
            while (temp):
                print(" -> {}".format(temp.vertex), end=" ")
                temp = temp.next
            print()


def main():
    V = 5
    graph = Graph(V)
    graph.add_node_edge(0, 1)
    graph.add_node_edge(1, 2)
    graph.add_node_edge(2, 3)
    graph.add_node_edge(3, 4)
    graph.add_node_edge(4, 0)
    graph.add_node_edge(1, 3)
    graph.add_node_edge(4, 1)
    graph.display_graph()


if __name__ == '__main__':
    main()
