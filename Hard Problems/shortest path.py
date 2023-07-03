
###Graphs

class Node(object):
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):  #takes in 2 nodes
        self.src = src
        self.dest = dest
    def get_source(self):
        return self.src
    def get_destination(self):
        return self.dest
    def __str__(self):
        return self.src.get_name() + "->" + self.dest.get_name()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):  #takes in 2 nodes and a weight default to 1.0
        super().__init__(src, dest)
        self.weight = weight
    def get_weight(self):
        return self.weight
    def __str__(self):
        return self.src.get_name() + "->(" + str(self.weight) + ")" + self.dest.get_name()

class Digraph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def add_node(self, node):
        if node in self.nodes:
            raise ValueError("Duplicate")
        else:
            self.nodes.append(node)
            self.edges[node] = []
    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if src not in self.nodes or dest not in self.nodes:
            raise ValueError("Node not in graph")
        else:
            self.edges[src].append(dest)
    def children_of(self, node):
        return self.edges[node]
    def has_node(self, node):
        return node in self.nodes
    def __str__(self):
        result = ""
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.get_name() + "->" + dest.get_name() + "\n"
        return result[:-1]

class Graph(Digraph):
    def add_edge(self, edge):
        super().add_edge(edge)
        reverse = Edge(edge.get_destination(), edge.get_source())
        super().add_edge(reverse)

def print_path(path):
    result = ""
    for i in range(len(path)):
        result += str(path[i])
        result += "->"
    return result[:-2]

def DFS(graph, start, end, path, shortest):
    path = path + [start]
    print(print_path(path))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def BFS(graph, start, end):
    initPath = [start]
    pathQ = [initPath]

    while len(pathQ) != 0:
        tmp = pathQ.pop(0)
        print(print_path(tmp))
        print("hi")
        last_node = tmp[-1]
        if last_node == end:
            return tmp
        for next_node in graph.children_of(last_node):
            if next_node not in tmp:
                new_path = tmp + [next_node]
                pathQ.append(new_path)
    return None

##        
##    def shortest_path(self, loc1, loc2):
##        def DFS(start, end, path, shortest, cur_dist, min_dist):
##            path = path + [start]
##            if start == end:
##                return (path, cur_dist)
##            for node in self.edges[start]:
##                if node not in path:
##                    if shortest == None or (cur_dist + self.get_distance(start, node)) < min_dist:
##                        new_path, dist = DFS(node, end, path, shortest, (cur_dist + self.get_distance(start, node)), min_dist)
##                        if new_path != None:
##                            print(min_dist)
##                            shortest = new_path
##                            min_dist = dist
##            return (shortest, min_dist)
##        a, b = DFS(loc1, loc2, [], None, 0, 0)
##        print(b)
##        return b





flight_plans = Graph()

singapore = Node("Singapore")
seoul = Node("Seoul")
tokyo = Node("Tokyo")
sanfrancisco = Node("San Francisco")
sg_to_tokyo = Edge(singapore, tokyo)
tokyo_to_seoul = Edge(tokyo, seoul)


flight_plans.add_node(singapore)
flight_plans.add_node(tokyo)
flight_plans.add_node(seoul)
flight_plans.add_edge(sg_to_tokyo)
flight_plans.add_edge(tokyo_to_seoul)

#print(DFS(flight_plans, singapore, seoul, [], None))
print(BFS(flight_plans, singapore, seoul))
