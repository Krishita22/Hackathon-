def run_pulser_simulation(Q):
    print("\n🔷 QUBO Matrix (for Pulser):\n")
    for (i, j), value in Q.items():
        print(f"Q[{i}, {j}] = {value:.2f}")
