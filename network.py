import networkx as nx

def create_network():
    G = nx.Graph()

    # Add nodes
    for i in range(6):
        G.add_node(i, pressure=50)

    # Add pipes with resistance
    edges = [
        (0,1,0.5),
        (1,2,0.3),
        (1,3,0.4),
        (2,4,0.6),
        (3,5,0.5)
    ]

    for u, v, r in edges:
        G.add_edge(u, v, resistance=r, flow=0)

    return G