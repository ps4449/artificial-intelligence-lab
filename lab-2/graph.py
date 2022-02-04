class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] 
                              for row in range(vertices)] 
  
    # A utility function to check if the current colour assignment 
    # is valid for vertex v 
    def isValid(self, v, colour, c): 
        for i in range(self.V): 
            if self.graph[v][i] == 1 and colour[i] == c: 
                return False
        return True
      
    # A recursive utility function to solve m 
    # colouring  problem 
    def graphColourUtil(self, m, colour, v): 
        if v == self.V: 
            return True
  
        for c in range(1, m+1): 
            if self.isValid(v, colour, c): 
                colour[v] = c 
                if self.graphColourUtil(m, colour, v+1): 
                    return True
                colour[v] = 0
  
    def graphColouring(self, m): 
        colour = [0] * self.V 
        if self.graphColourUtil(m, colour, 0) == False: 
            return False
  
        # Print the solution 
        print(f"This problem uses {m} colours to colour {self.V} vertices.")
        print("Solution exists.")
        print("Following are the assigned colours:")
        for i in range(0, 4): 
            print(f"Vertex = {i}", end=", ")
            print(f"Colour = {colour[i]}")
        return True
  
# Driver Code 
g = Graph(4)
g.graph([0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0] 
m = 3
g.graphColouring(m) 
