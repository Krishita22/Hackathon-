def generate_qubo(G, num_colors=3):
    Q = {}
    penalty = 1.0

    for node in G.nodes:
        for c1 in range(num_colors):
            for c2 in range(num_colors):
                i = node * num_colors + c1
                j = node * num_colors + c2
                if c1 == c2:
                    Q[(i, j)] = Q.get((i, j), 0) - penalty
                else:
                    Q[(i, j)] = Q.get((i, j), 0) + penalty

    for u, v in G.edges:
        for c in range(num_colors):
            i = u * num_colors + c
            j = v * num_colors + c
            Q[(i, j)] = Q.get((i, j), 0) + penalty

    return Q
