from collections import deque


def build_graph(chats):
    graph = {}

    for chat in chats:
        for person in chat:
            if person not in graph:
                graph[person] = set()

        for person_a in chat:
            for person_b in chat:
                if person_a != person_b:
                    graph[person_a].add(person_b)

    return graph


def can_reach(chats, start, end):
    if start == end:
        return True

    graph = build_graph(chats)

    if start not in graph or end not in graph:
        return False

    queue = deque([start])
    visited = {start}

    while queue:
        current_person = queue.popleft()

        for neighbor in graph[current_person]:
            if neighbor == end:
                return True

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False

chats = (
    ("Dwayne", "Minh", "Aisha"),
    ("Priya", "Noor", "Dwayne"),
    ("Juan", "Jelly"),
    ("Allison", "Gus"),
    ("Priya", "Bethel", "Janelle", "Ken"),
    ("Noor", "Kimi", "Rubens"),
    ("Minh", "Elora"),
    ("Allison", "Gus", "Juan"),
    ("Priya", "Noor"),
)
assert can_reach(chats, "Janelle", "Elora") == True
assert can_reach(chats, "Bethel", "Gus") == False
assert can_reach(chats, "Priya", "Noor") == True
assert can_reach(chats, "Rubens", "Ken") == True
assert can_reach(chats, "Allison", "Priya") == False

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
