class Graph():
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        else:
            return False

    def display(self):
        for i in self.adjacency_list:
            print(i, ": ", self.adjacency_list[i])

    def add_edge(self, v1, v2):
        if v1 in self.adjacency_list.keys() and v2 in self.adjacency_list.keys():
            self.adjacency_list[v1].append(v2)
            self.adjacency_list[v2].append(v1)
            return True
        else:
            return False

    def remove_edge(self, v1, v2):
        if v1 in self.adjacency_list.keys() and v2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[v1].remove(v2)
                self.adjacency_list[v2].remove(v1)
                return True
            except ValueError:
                pass
            return True
        else:
            return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for i in self.adjacency_list[vertex]:
                self.adjacency_list[i].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        else:
            return False

g1 = Graph()
