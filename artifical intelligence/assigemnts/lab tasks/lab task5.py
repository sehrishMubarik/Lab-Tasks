tree = {
    'A':['B' , 'C'],
    'B': ['D' , 'E'],
    'C':['F' , 'G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}
 
Visited = set()
def dfs(tree, visited, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for i in tree[node]:
            dfs(tree, visited, i )
dfs(tree, Visited, 'A')

# inorder
tree = {
    'A': ['B', 'C'],
    'B': ['D' , 'E'],
    'C': ['F', 'G'],
    'D':[] ,
    'E':[] ,
    'F':[] ,
    'G':[]
}

visited = set()
def inorder_dfs(visited, tree , node):
    if node not in visited:
        n = tree[node]
        if len(n) > 0:
            inorder_dfs(visited, tree, n[0])
        print(node)
        visited.add(node)
        if len(n) > 1:
            inorder_dfs(visited , tree, n[1])
                    
inorder_dfs(visited, tree , 'A')

# post_order
tree = {
    'A': ['B', 'C'],
    'B': ['D' , 'E'],
    'C': ['F', 'G'],
    'D':[] ,
    'E':[] ,
    'F':[] ,
    'G':[]
}

visited = set()
def postorder_dfs(visited, tree , node):
    if node not in visited:
        n = tree[node]
        if len(n) > 0:
            postorder_dfs(visited, tree, n[0])
        if len(n) > 1:
            postorder_dfs(visited , tree, n[1])
        print(node)
        visited.add(node)
                    
postorder_dfs(visited, tree , 'A')

