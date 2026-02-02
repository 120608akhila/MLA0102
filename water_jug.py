from collections import deque

def water_jug_problem(jug1_cap, jug2_cap, target):
    visited = set()
    queue = deque()

    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()

        if jug1 == target or jug2 == target:
            path.append((jug1, jug2))
            print("Solution Path:")
            for step in path:
                print(step)
            return

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        states = [
            (jug1_cap, jug2),
            (jug1, jug2_cap),
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, jug2_cap - jug2),
             jug2 + min(jug1, jug2_cap - jug2)),
            (jug1 + min(jug2, jug1_cap - jug1),
             jug2 - min(jug2, jug1_cap - jug1))
        ]

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path + [(jug1, jug2)]))

    print("No solution possible")


water_jug_problem(4, 3, 2)
