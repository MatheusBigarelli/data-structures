class Graph:
    def __init__(self, vertices=None, edges=None):
        if type(vertices) is list:
            self.vertex_type = self.check_vertex_array_content_type(vertices)
            self.vertices = vertices
        elif type(vertices) is None:
            self.vertices = []

        if type(edges) is list:
            for edge in edges:
                self.edge_type_is_valid(edge)
                self.edge_has_valid_vertices(edge)
            self.edges = edges
        elif type(edges) is None:
            self.edges = []




    def check_vertex_array_content_type(self, array):
        if len(array) > 0:
            element_type = type(array[0])
            for element in array:
                if element_type is str and element == '':
                    raise ValueError('Value Error - Vertex name cannot be empty string')

                if type(element) is not element_type:
                    raise TypeError('Type Error - Vertices are not the same type')
        else:
            raise ValueError('Value Error - Passed empty list of vertices')

        return element_type


    def edge_type_is_valid(self, edge):
        if type(edge) is not tuple:
            raise TypeError('Edges must be tuples of vertices')

    def edge_has_valid_vertices(self, edge):
        if len(edge) > 2:
            raise ValueError('Value Error - More than two vertices passed')
        if type(edge[0]) != self.vertex_type or type(edge[1]) != self.vertex_type:
            raise TypeError('Type Error - Edge has vertices of wrong type')

        if edge[0] not in self.vertices or edge[1] not in self.vertices:
            raise ValueError('Value Error - Vertices not found in graph')

    def add_vertex(self, vertex):
        if type(vertex) == self.vertex_type:
            self.vertices.append(vertex)
        elif type(vertex) is list:
            self.check_vertex_array_content_type(vertex)
            for element in vertex:
                self.vertices.append(element)
        else:
            raise ValueError('Value Error - Vertex type is different from the others')


    def add_edge(self, edge):
        self.edge_type_is_valid(edge)
        self.edge_has_valid_vertices(edge)
        self.edges.append(edge)


    def __str__(self):
        return 'Vertices {vertices}\nEdges: {edges}'.format(vertices=self.vertices, edges=self.edges)

if __name__ == '__main__':
    graph = Graph(['a', 'b'], [('a', 'b')])
    graph.add_vertex('c')
    graph.add_edge(('a', 'c'))
    print(graph)
