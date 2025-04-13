import networkx as nx

def create_sample_graph():
    G = nx.Graph()
    G.add_edges_from([
        (0, 1), (1, 2), (2, 3), (3, 0),
        (0, 2)
    ])
    return G
