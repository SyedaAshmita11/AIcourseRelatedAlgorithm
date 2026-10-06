# Prim's Algorithm - Cheapest road network connecting all places
# Same road map is used in all three files (distance in km = road length to build).
# No library used.

graph = {
    "University":  [("Bus Stand", 3), ("Market", 5)],
    "Bus Stand":   [("University", 3), ("Market", 2), ("Launch Ghat", 6)],
    "Market":      [("University", 5), ("Bus Stand", 2), ("Hospital", 4)],
    "Hospital":    [("Market", 4), ("Launch Ghat", 3)],
    "Launch Ghat": [("Bus Stand", 6), ("Hospital", 3)],
}


def prims(graph, start):
    in_tree = {}
    for place in graph:
        in_tree[place] = False
    in_tree[start] = True

    mst_edges = []
    total = 0

    while len(mst_edges) < len(graph) - 1:
        best = None  # (from, to, length)
        # check every road going from connected places to unconnected places
        for u in graph:
            if in_tree[u]:
                for v, length in graph[u]:
                    if not in_tree[v]:
                        if best is None or length < best[2]:
                            best = (u, v, length)
        if best is None:
            break
        u, v, length = best
        in_tree[v] = True
        mst_edges.append(best)
        total += length
    return mst_edges, total


if __name__ == "__main__":
    edges, total = prims(graph, "University")
    print("Cheapest road network (Prim's, start = University)")
    print("-" * 50)
    for u, v, length in edges:
        print(f"{u:12} --- {v:12}: {length} km")
    print("-" * 50)
    print("Total road length:", total, "km")
