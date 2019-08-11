class Graph:

    class Vertex:
        __slots__ = '_element'

        def __init__(self, element):
            self._element = element

        def element(self):
            return self._element

        def __hash__(self):
            return hash(id(self))


    class Edge:
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, origin, destination, element):
            self._origin = origin
            self._destination = destination
            self._element = element

        def endpoint(self):
            return (self._origin, self._destination)

        def opposite(self, vertex):
            return self._destination if vertex is self._origin else self._origin

        def element(self):
            return self._element

        def __hash__(self):
            return hash((self._origin, self._destination))

    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        if not self._outgoing: return 0
        total = 0
        for  vertex in self._outgoing:
            total += len(self._outgoing[vertex])
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, v1, v2):
        return self._outgoing[v1].get(v2)

    def degree(self, vertex, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[vertex])

    def incident_edges(self, vertex, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[vertex].values():
            yield edge

    def insert_vertex(self, element=None):
        vertex = self.Vertex(element)
        self._outgoing[vertex] = {}
        if self.is_directed():
            self._incoming[vertex] = {}
        return vertex

    def insert_edge(self, origin, destination, element):
        edge = self.Edge(origin, destination, element)
        self._outgoing[origin][destination] = edge
        self._incoming[destination][origin] = edge

    def depth_first_search(self, vertex, visited_vertices={}):
        if not visited_vertices:
            visited_vertices[vertex] = None

        for edge in self.incident_edges(vertex):
            opposite_vertex = edge.opposite(vertex)
            if opposite_vertex not in visited_vertices:
                visited_vertices[opposite_vertex] = edge
                return self.depth_first_search(opposite_vertex, visited_vertices)

    def construct_path(self, origin, vertex, discovered):
        path = []
        if vertex in discovered:
            path.append(vertex)
            walk = vertex
            while walk is not origin:
                edge = discovered[walk]
                parent = edge.opposite(walk)
                path.append(parent)
                walk = parent
            path.reverse()
        return path


def depth_first_search(g, u, discovered):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            depth_first_search(g, v, discovered)


g = Graph()
print(g)
print('is directed?', g.is_directed())
v1 = g.insert_vertex('first vertex')
print(v1)
v2 = g.insert_vertex('second vertex')
g.insert_edge(v1, v2, 'edge1')
print('vertex count', g.vertex_count())

print('edge cound', g.edge_count())
v3 = g.insert_vertex('third vertex')
print('edges', g.edges())

print('path:', g.construct_path(v1, v2))

i = 1
for v in g.vertices():
    print('vertex element {}:'.format(i), v.element())
    i += 1