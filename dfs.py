import random
import string

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		
		self.discovery = 0
		self.finish = 0
		self.color = 'black'
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	vertices = {}
	time = 0
	terminar = False
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
			return True
		else:
			return False
			
	def print_graph(self):
		graf = []
		for key in sorted(list(self.vertices.keys())):
			graf.append((key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].discovery) + "/" + str(self.vertices[key].finish)))
		#print graf
		return graf

	def _dfs(self, vertex):
		global time
		vertex.color = 'red'
		vertex.discovery = time
		time += 1
		for v in vertex.neighbors:
			if self.vertices[v].color == 'black':
				self._dfs(self.vertices[v])
			if self.vertices[v].color == 'yellow':
				#print 'Tesoro encontrado en '+ self.vertices[v].name
				#g.print_graph()
				self.terminar = True
				return self.vertices[v]

		vertex.color = 'blue'
		vertex.finish = time
		time += 1
		
	def dfs(self, vertex):
		global time
		if self.terminar:
			return v
		else:
			time = 1
			v = self._dfs(vertex)

def main(x):
			
	g = Graph()
	# print(str(len(g.vertices)))
	#tesoro = chr(random.randrange(65,73))
	tesoro = x
	a = Vertex('A')
	g.add_vertex(a)
	text = ""
	if tesoro == 'A':
		text = ["Tesoro encontrado en A"]
		text += g.print_graph()
		g.terminar = True
		return text
		#raise SystemExit
	#g.add_vertex(Vertex('B'))

	#print tesoro
	for i in range(ord('A'), ord('K')):
		v = Vertex(chr(i))
		if chr(i) == tesoro: #agrega el tesoro al vertice
			v.color = 'yellow'
		g.add_vertex(v)

	edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
	for edge in edges:
		g.add_edge(edge[:1], edge[1:])
		
	b = g.dfs(a)
	return g.print_graph