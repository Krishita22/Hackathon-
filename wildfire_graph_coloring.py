import networkx as nx
from dwave.system import DWaveSampler, EmbeddingComposite
import dimod
import json

# Load graph data
with open("data/wildfire_regions_graph.json", "r") as f:
    graph_data = json.load(f)

G = nx.node_link_graph(graph_data)

# Number of colors (e.g., 3 resource types)
num_colors = 3

# QUBO formulation for graph coloring
bqm = dimod.BinaryQuadraticModel({}, {}, 0.0, dimod.BINARY)

for node in G.nodes:
    for color in range(num_colors):
        bqm.add_variable((node, color), -1.0)
        for other_color in range(color + 1, num_colors):
            bqm.add_interaction((node, color), (node, other_color), 2.0)

for u, v in G.edges:
    for color in range(num_colors):
        bqm.add_interaction((u, color), (v, color), 1.0)

# Sample using D-Wave sampler (replace with simulated sampler if testing)
sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm, num_reads=100)
best_sample = sampleset.first.sample

# Display results
coloring = {}
for (node, color), val in best_sample.items():
    if val:
        coloring[node] = color

print("Graph Coloring Result:")
for region, color in coloring.items():
    print(f"Region {region}: Color {color}")
