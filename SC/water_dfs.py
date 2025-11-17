
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

def water_jug_bfs(capacity1, capacity2, target):
    visited = set()
    queue = deque([(0, 0, [(0, 0)])])
    visited.add((0, 0))

    while queue:
        jug1, jug2, path = queue.popleft()

        if jug1 == target or jug2 == target:
            return path

        next_states = [
            (capacity1, jug2),
            (jug1, capacity2),
            (0, jug2),
            (jug1, 0),
            (max(0, jug1 - (capacity2 - jug2)), min(capacity2, jug1 + jug2)),
            (min(capacity1, jug1 + jug2), max(0, jug2 - (capacity1 - jug1)))
        ]

        for next_jug1, next_jug2 in next_states:
            if (next_jug1, next_jug2) not in visited:
                visited.add((next_jug1, next_jug2))
                queue.append((next_jug1, next_jug2, path + [(next_jug1, next_jug2)]))

    return None

def visualize_bfs_solution(solution):
    G = nx.DiGraph()

    for i in range(len(solution) - 1):
        G.add_edge(solution[i], solution[i + 1])

    pos = nx.spring_layout(G)

    plt.figure(figsize=(10, 8))

    nx.draw(G, pos, with_labels=True, node_color='lightgreen',
            node_size=1500, font_size=10, font_weight='bold')
    nx.draw_networkx_edges(G, pos, edgelist=list(G.edges()),
                          edge_color='blue', width=2, arrows=True, arrowsize=20)

    plt.title("Water Jug Problem - Optimal BFS Solution Path", fontsize=14,
fontweight='bold')
    plt.tight_layout()
    plt.show()

def get_user_input():
    print("Water Jug Problem - Optimal BFS Solution")
    print("=" * 45)

    capacity1 = int(input("Enter capacity of Jug 1: "))
    capacity2 = int(input("Enter capacity of Jug 2: "))
    target = int(input("Enter target amount to measure: "))

    print(f"\nJug 1 capacity: {capacity1} liters")
    print(f"Jug 2 capacity: {capacity2} liters")
    print(f"Target: {target} liters")

    return capacity1, capacity2, target

def main():
    capacity1, capacity2, target = get_user_input()

    if target > max(capacity1, capacity2):
        print(f"\nError: Target {target} is greater than the maximum jug capacity {max(capacity1, capacity2)}")
        print("No solution possible!")
        return

    print("\nRunning BFS algorithm for optimal solution...")
    solution = water_jug_bfs(capacity1, capacity2, target)

    if solution:
        print(f"\nSolution found in {len(solution)} steps:")
        print("Step-by-step solution:")
        for i, step in enumerate(solution):
            print(f"Step {i+1}: Jug1={step[0]}, Jug2={step[1]}")

        print("\nDisplaying graph visualization...")
        visualize_bfs_solution(solution)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()