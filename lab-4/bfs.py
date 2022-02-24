from collections import defaultdict
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	# Function to print a BFS of graph
	def BFS(self, s):
	# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)
		queue = [] # Create a queue for BFS

		# Mark the source node as visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:
			# Dequeue a vertex from queue and print it
			s = queue.pop(0)
			print (s, end = " ")

			# Get all adjacent vertices of the dequeued vertex s. 
			# If a adjacent has not been visited, then mark it visited 
			# and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(5, 5)

print("Following is Breadth First Traversal (starting from vertex 0): ")
g.BFS(0)
