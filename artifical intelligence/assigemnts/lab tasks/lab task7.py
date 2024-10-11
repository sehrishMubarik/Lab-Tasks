graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 5)],
    'C': [('A', 4), ('D', 2), ('E', 7)],
    'D': [('B', 5), ('C', 2), ('E', 3), ('F', 2)],
    'E': [('C', 7), ('D', 3), ('F', 1)],
    'F': [('D', 2), ('E', 1)]
}

def get_neighbour(v):
    return graph.get(v, [])

def h(n):
    h_dist = {
        'A': 12,
        'B': 41,
        'C': 11,
        'D': 21,
        'E': 20,
        'F': 19
    }
    return h_dist[n]

def a_star(start_node, end_node):
    open_set = set([start_node])  
    close_set = set()  
    g = {}  
    g[start_node] = 0

    parent = {}  
    parent[start_node] = start_node

    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n is None or g[v] + h(v) < g[n] + h(n):
                n = v

        if n is None:
            print("Path does not exist")
            return None
        if n == end_node:
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]
            path.append(start_node)
            path.reverse()
            print("Path found:", path)
            return path
        for (m, weight) in get_neighbour(n):
            if m not in open_set and m not in close_set:
                open_set.add(m)
                g[m] = g[n] + weight
                parent[m] = n
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parent[m] = n
                    if m in close_set:
                        close_set.remove(m)
                        open_set.add(m)
        open_set.remove(n)
        close_set.add(n)

    print("Path not found")
    return None
a_star('A', 'F')