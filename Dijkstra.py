import collections
import math

def dijkstra(graph, start):
    S = set()

    shortest_paths = dict.fromkeys(list(graph.vertices), float("inf"))
    previous = dict.fromkeys(list(graph.vertices), None)

    shortest_paths[start] = 0

    while S != graph.vertices:
        v = min((set(shortest_paths.keys()) - S), key=shortest_paths.get)
        for neighbour in set(graph.edges[v]) - S:
            new_path = shortest_paths[v] + graph.weights[v, neighbour]
            if new_path < shortest_paths[neighbour]:
                shortest_paths[neighbour] = new_path

                previous[neighbour] = v
        S.add(v)
    return (shortest_paths, previous)

def shortest_path(graph, start, end):
    paths, previous = dijkstra(graph, start)

    path = []
    vertex = end

    while vertex is not None:
        path.append(vertex)
        vertex = previous[vertex]
    path.reverse()
    return path
