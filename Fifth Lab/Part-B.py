from collections import deque
CAPACITY_X = 5
CAPACITY_Y = 3
def get_next_states(state):
    x, y = state
    next_states = []
    if x < CAPACITY_X:
        next_states.append(((CAPACITY_X, y), "Fill 5-gallon jug"))
    if y < CAPACITY_Y:
        next_states.append(((x, CAPACITY_Y), "Fill 3-gallon jug"))
    if x > 0:
        next_states.append(((0, y), "Empty 5-gallon jug"))
    if y > 0:
        next_states.append(((x, 0), "Empty 3-gallon jug"))
    amount = min(x, CAPACITY_Y - y)
    if amount > 0:
        next_states.append(
            ((x - amount, y + amount), "Pour 5-gallon jug into 3-gallon jug")
        )
    amount = min(y, CAPACITY_X - x)
    if amount > 0:
        next_states.append(
            ((x + amount, y - amount), "Pour 3-gallon jug into 5-gallon jug")
        )
    return next_states
def bfs():
    initial_state = (0, 0)
    queue = deque()
    queue.append((initial_state, []))
    visited = set()
    visited.add(initial_state)
    while queue:
        current_state, path = queue.popleft()
        x, y = current_state
        if x == 4:
            return path
        for next_state, action in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                new_path = path + [
                    (current_state, action, next_state)
                ]
                queue.append((next_state, new_path))
    return None
solution = bfs()
if solution:
    print("Water Jug Problem")
    print("5-Gallon Jug and 3-Gallon Jug")
    print("\nSolution:\n")
    step = 1
    for current, action, next_state in solution:
        print("Step", step)
        print("Current State:", current)
        print("Action:", action)
        print("Next State:", next_state)
        print()
        step += 1
    print("Total Steps:", len(solution))
    print("Goal State:", solution[-1][2])
else:
    print("No solution found.")