# Hackathon
# Quantum Graph Coloring for Wildfire Risk Minimization

This project demonstrates how quantum computing, using D-Wave's quantum annealer, can be applied to solve a graph coloring problem aimed at minimizing wildfire spread across regions.

### Problem
We model regions affected by wildfires as a graph, where:
- Nodes = regions
- Edges = shared borders
- Colors = firefighting resource types or risk levels

### Goal
Color the graph such that no two adjacent regions share the same firefighting strategy (color), minimizing risk and resource conflict.

### Tech
- D-Wave Ocean SDK
- NetworkX
- Python 3.10+

### Run
```
pip install -r requirements.txt
python wildfire_graph_coloring.py
```
