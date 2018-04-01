def find_circle(num_nodes, edges):
    nodes = [list() for i in range(num_nodes)] 
    
    for v1, v2 in edges:
        nodes[v1].append(v2)
        nodes[v2].append(v1)

    print(nodes)

    for i in range(num_nodes):
        # stack = []
        prev_node = -1
        dfs(i, nodes, [], prev_node)


def dfs(start, nodes, stack, prev_node):
    for next_node in nodes[start]:
        if next_node == prev_node:
            continue
        if next_node in stack:
            print(stack)Å
            return
        tmp = stack[:]
        tmp.append(next_node)
        dfs(next_node, nodes, tmp, start)


edges=[[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8]]    
find_circle(10, edges)