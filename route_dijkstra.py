# Dijkstra's Algorithm - Shortest route from one place to all others
# Same road map is used in all three files (distance in km).
# No library used.

INF = 999999

# Road map: place -> list of (neighbor, distance)
graph = {
    "University":  [("Bus Stand", 3), ("Market", 5)],
    "Bus Stand":   [("University", 3), ("Market", 2), ("Launch Ghat", 6)],
    "Market":      [("University", 5), ("Bus Stand", 2), ("Hospital", 4)],
    "Hospital":    [("Market", 4), ("Launch Ghat", 3)],
    "Launch Ghat": [("Bus Stand", 6), ("Hospital", 3)],
}


def dijkstra(graph, source):
    dist = {}
    parent = {}
    visited = {}
    for place in graph:
        dist[place] = INF
        parent[place] = None
        visited[place] = False
    dist[source] = 0

    for _ in range(len(graph)):
        # pick unvisited place with smallest distance
        current = None
        for place in graph:
            if not visited[place]:
                if current is None or dist[place] < dist[current]:
                    current = place
        if current is None or dist[current] == INF:
            break
        visited[current] = True

        # update neighbors
        for neighbor, weight in graph[current]:
            if dist[current] + weight < dist[neighbor]:
                dist[neighbor] = dist[current] + weight
                parent[neighbor] = current
    return dist, parent


def get_path(parent, target):
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    path.reverse()
    return path


if __name__ == "__main__":
    source = "University"
    dist, parent = dijkstra(graph, source)
    print("Shortest routes from", source)
    print("-" * 50)
    for place in graph:
        print(f"{place:12}: {dist[place]:2} km   {' -> '.join(get_path(parent, place))}")
