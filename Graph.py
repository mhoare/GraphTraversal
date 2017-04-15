graph = {
        'A' : {'B' : 1, 'C': 1},
        'B' : {'C' : 1, 'D' : 1},
        'C' : {'D' : 1},
        'D' : {'C' : 1},
        'E' : {'F' : 1},
        'F' : {'C' : 1}
        }

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path: return new_path
    return None

def find_cost(graph, path):
    cost = 0
    for x in range(0, len(path)-1):
        cost += graph[path[x]][path[x+1]]
    return cost

print """
* * * * * * EXAMPLE * * * * * *

Example showing find a path (not neccesarily the shortest) 
between vertex A and D. 
Also calculates the cost of the path generated.

Graph: 
"""
print graph
path = find_path(graph, 'A', 'D')
print """
Path: 
"""
print path 
print "Cost: " + str(find_cost(graph, path))
print """
* * * * * * EXAMPLE * * * * * *

Example showing a result where a path couldn't be found 
- between vertex A and vertex F

"""

print "Result: " + str(find_path(graph, 'A', 'F'))
