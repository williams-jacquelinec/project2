# Name: Jacqueline Williams
# BMI 203 Project 2

import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None

        """

        # creating objects for the graph, nodes I've visited, and the queue
        G = self.graph
        visited = []
        queue = []

        # keeping track of the parent nodes (if end != None)
        # key-value pair = {child:parent, child:parent, etc.}
        parent_nodes = {}
        parent_nodes[start] = None

        # initiating the shortest_path object; it is False now because I haven't gone anywhere yet
        my_path = False

        # adding the start node to my visited and queue lists
        visited.append(start)
        queue.append(start)

        while queue:
            current_node = queue.pop(0)   # dequeue current node

            if current_node == end:    # when we reach the end node, stop iterating
                my_path = True
                break

            for neighbor in G[current_node]:
                if neighbor not in visited:      # for each unvisited neighbor of current node (G[s])
                    visited.append(neighbor)
                    queue.append(neighbor)
                    parent_nodes[neighbor] = current_node  # stores the parent node (current_node) of the neighbor node

        # finding the shortest path
        if end and my_path:
            shortest_path = []

            if my_path:
                end_ = end
                shortest_path.append(end_)

                while parent_nodes[end_] is not None:     # while the child value still has a parent... #reminder: start node has no parent
                    shortest_path.append(parent_nodes[end_])
                    end_ = parent_nodes[end_]      # updating the end node to reflect the parent; keeps iterating through the path backwards

                shortest_path.reverse()
            return shortest_path

        elif end and not my_path:   # there is no path to the end node
            return None

        else:
            return visited     # there is no end node indicated

