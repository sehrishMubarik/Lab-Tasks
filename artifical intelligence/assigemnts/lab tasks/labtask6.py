tree = {
    'A': ['B', 'C'],
    'B': ['D' , 'E'],
    'C': ['F', 'G'],
    'D':[] ,
    'E':[] ,
    'F':[] ,
    'G':[]
}
 
visited = []
explore=[]

def bfs(tree, visited , node):
        visited.append(node)
        explore.append(node)
        while explore:
            m = explore.pop(0)
            print(m)
            for n in tree[m]:
                if n not in visited:
                    visited.append(n)
                    explore.append(n)
                                                      
bfs(tree, visited , 'A')

# without node
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

visited = []

def bfs_level(tree, current_position):
    next_level = []
    
    for node in current_position:
        if node not in visited:
            print(node)
            visited.append(node)
            next_level.extend(tree[node])
    if next_level:
        bfs_level(tree, next_level)
        
bfs_level(tree, ['A'])