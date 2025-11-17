
from collections import deque

def bfs(a, b, target):
    visited = set()
    q = deque()
    q.append(((0, 0), []))
    while q:
        (x, y), path = q.popleft()
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
                q.append((new_state, path + [(x, y, action)]))
    print("No solution possible")

a = int(input("Enter capacity of Jug 1: "))
b = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter amount of water to be measured: "))
print("Steps to measure the target:")
bfs(a, b, target)