import heapq

def heuristic(x, y, target):
    return abs(x - target) + abs(y - target)

def astar(a, b, target):
    visited = set()
    pq = []
    heapq.heappush(pq, (0, (0, 0), []))
    while pq:
        cost, (x, y), path = heapq.heappop(pq)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if x == target or y == target:
            for step in path + [(x, y, "Goal reached")]:
                if len(step) == 3:
                    print(f"{step[2]} -> ({step[0]}, {step[1]})")
                else:
                    print(step)
            return
        states = []
        states.append(((a, y), "Fill Jug 1"))
        states.append(((x, b), "Fill Jug 2"))
        states.append(((0, y), "Empty Jug 1"))
        states.append(((x, 0), "Empty Jug 2"))
        pour = min(x, b - y)
        states.append(((x - pour, y + pour), "Pour Jug 1 → Jug 2"))
        pour = min(y, a - x)
        states.append(((x + pour, y - pour), "Pour Jug 2 → Jug 1"))
        for new_state, action in states:
            if new_state not in visited:
                new_cost = cost + 1 + heuristic(new_state[0], new_state[1], target)
                heapq.heappush(pq, (new_cost, new_state, path + [(x, y, action)]))
    print("No solution possible")

a = int(input("Enter capacity of Jug 1: "))
b = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter amount of water to be measured: "))
astar(a, b, target)