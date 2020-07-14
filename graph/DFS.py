class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.graph = [None] * self.v

    def addEdge(self, src, des):
        node = Node(des)
        node.next = self.graph[src]
        self.graph[src] = node

        node = Node(src)
        node.next = self.graph[des]
        self.graph[des] = node

    def dfsHelper(self, s, visited):
        visited[s] = True
        print(s, end=" ")

        for i in range(self.v):
            if not visited[i]:
                self.dfsHelper(i, visited)

    def dfs(self, s):
        visited = [False] * len(self.graph)
        self.dfsHelper(s, visited)

    def printGraph(self):
        for i in range(self.v):
            temp = self.graph[i]
            while temp:
                print("->{}".format(temp.data), end="")
                temp = temp.next
            print("")


def main():
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.printGraph()
    print("--The dfs order is")
    g.dfs(2)


if __name__ == '__main__':
    main()
