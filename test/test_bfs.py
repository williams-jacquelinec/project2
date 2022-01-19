# write tests for bfs
import pytest
from search import graph

@pytest.fixture
def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    bfs_traversal = Graph('data/tiny_network.adjlist').bfs('Atul Butte', end=None)

    with open('data/tiny_network.adjlist', 'r') as data_file:
        lines = [l for l in data_file if not l.startswith('#')]

    assert len(bfs_traversal) == len(lines)  #assuming each line is a node (and each node it is connected to)

    

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    # test for nodes that are connected (and return the shortest path)
    bfs_shortest_path = Graph('data/citation_network.adjlist').bfs('Atul Butte', end='Jill Hollenbach')
    return bfs_shortest_path
    assert len(bfs_shortest_path) == 3

    # test for nodes that are not connected
    bfs_path = Graph('data/citation_network.adjlist').bfs('34720789', end='34966387')
    return bfs_path
    assert bfs_path == None
