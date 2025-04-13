from graph_utils import create_sample_graph
from qubo_utils import generate_qubo
from pulser_simulation import run_pulser_simulation

if __name__ == "__main__":
    G = create_sample_graph()
    Q = generate_qubo(G, num_colors=3)
    run_pulser_simulation(Q)
