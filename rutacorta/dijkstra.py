class Vertex:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.neighbors = []
        self.distance = 10000000000
        self.father = None

    def add_neighbor(self, v, w):
        if v not in self.neighbors:
            self.neighbors.append([v,w])
            
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v, w):
        for key, value in self.vertices.items():
            if key == u.name:
                value.add_neighbor(v, w)
            #if key == v:
                #value.add_neighbor(u)
    
    def print_graph(self):
        for key, v in self.vertices.items():
            print v.name + " " + str(v.distance) + " - Father " + str(v.father)


def Dijkstra(graph, start):
    for key, n in graph.vertices.items():
        n.distance = 10000000000
        n.father = None
        n.visited = False

    start.distance = 0
    cola = [[start,start.distance]]
    while cola:
        u = cola[0]
        u[0].visited = True
        cola.remove(u)
        v = u[0].neighbors
        for v in u[0].neighbors:
            if not v[0].visited and v[0].distance > u[0].distance + v[1]:
                v[0].distance = u[0].distance + v[1]
                v[0].father = u[0].name
                cola.append(v)

def shortestpath(graph, u, v, l):
    if u.name != v.name:
        new_v = graph.vertices[v.father]
        shortestpath(graph, u, new_v, l)
        l.append(v.name)
        #print v.name
    else:
        l.append(u.name)
    return l
        #print u.name


def main(origen, destino):
    g = Graph()
    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    e = Vertex('E')
    g.add_vertex(a)
    g.add_vertex(b)
    g.add_vertex(c)
    g.add_vertex(d)
    g.add_vertex(e)

    g.add_edge(a,c,12)
    g.add_edge(a,d,60)
    g.add_edge(b,a,10)
    g.add_edge(c,b,20)
    g.add_edge(c,d,32)
    g.add_edge(e,a,7)

    if origen == 'A':
        nodo_origen = a
    elif origen == 'B':
        nodo_origen = b
    elif origen == 'C':
        nodo_origen = c
    elif origen == 'D':
        nodo_origen = d
    else:
        nodo_origen = e

    if destino == 'A':
        nodo_destino = a
    elif destino == 'B':
        nodo_destino = b
    elif destino == 'C':
        nodo_destino = c
    elif destino == 'D':
        nodo_destino = d
    else:
        nodo_destino = e
    
    Dijkstra(g, nodo_origen)
    
    l = []
    
    return shortestpath(g, nodo_origen, nodo_destino, l)
    
'''
if __name__=='__main__':
    main()
'''
