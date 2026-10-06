# Kruskal's Algorithm - Cheapest road network connecting all places
# Same road map is used in all three files (distance in km = road length to build).
# No library used.

places = ["University", "Bus Stand", "Market", "Hospital", "Launch Ghat"]

# Each road is listed once: (place1, place2, length)
roads = [
    ("University", "Bus Stand", 3),
    ("University", "Market", 5),
    ("Bus Stand", "Market", 2),
    ("Bus Stand", "Launch Ghat", 6),
    ("Market", "Hospital", 4),
    ("Hospital", "Launch Ghat", 3),
]


def sort_roads(roads):
    # selection sort: shortest road first
    roads = roads[:]
    for i in range(len(roads)):
        m = i
        for j in range(i + 1, len(roads)):
            if roads[j][2] < roads[m][2]:
                m = j
        roads[i], roads[m] = roads[m], roads[i]
    return roads


# ----- Union-Find: tells if two places are already connected -----
def find(parent, x):
    while parent[x] != x:
        x = parent[x]
    return x


def union(parent, a, b):
    ra, rb = find(parent, a), find(parent, b)
    if ra == rb:
        return False   # already connected -> cycle, skip this road
    parent[rb] = ra
    return True


def kruskal(places, roads):
    parent = {}
    for p in places:
        parent[p] = p

    mst_edges = []
    total = 0
    for u, v, length in sort_roads(roads):
        if union(parent, u, v):
            mst_edges.append((u, v, length))
            total += length
        if len(mst_edges) == len(places) - 1:
            break
    return mst_edges, total


if __name__ == "__main__":
    edges, total = kruskal(places, roads)
    print("Cheapest road network (Kruskal's)")
    print("-" * 50)
    for u, v, length in edges:
        print(f"{u:12} --- {v:12}: {length} km")
    print("-" * 50)
    print("Total road length:", total, "km")
