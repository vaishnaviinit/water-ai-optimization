import numpy as np

def simulate_network(G, pump_pressure):
    # Assign pressures
    for node in G.nodes:
        G.nodes[node]['pressure'] = pump_pressure - node * 3

    total_flow = 0

    for u, v in G.edges:
        p1 = G.nodes[u]['pressure']
        p2 = G.nodes[v]['pressure']
        r = G.edges[u, v]['resistance']

        flow = (p1 - p2) / r
        G.edges[u, v]['flow'] = flow
        total_flow += abs(flow)

    return G, total_flow


def leak_flow(pressure, leak_coeff):
    return leak_coeff * np.sqrt(max(pressure, 0))