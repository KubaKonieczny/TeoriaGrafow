import networkx as nx
from collections import deque


def graph_from_list_of_edges(file_io):
    graph = nx.DiGraph()
    for number, line in enumerate(file_io):
        from_node, to_node, weight = map(int, line.split())
        graph.add_edge(from_node, to_node, capacity=weight)
    return graph


def graph_from_adjacency_list(file_io):
    graph = nx.DiGraph()
    for number, line in enumerate(file_io):
        number += 1
        ar = list(map(int, line.split()))
        for i in range(0, len(ar), 2):
            graph.add_edge(number, ar[i], capacity=ar[i + 1])
    return graph


def path_between(graph, s, d):
    parent = {}
    path = []
    visited = [s]
    q = deque([s])
    des = d

    while q:
        v = q.popleft()
        for node in graph.adj[v]:
            if node not in visited:
                visited.append(node)
                q.append(node)
                parent[node] = v

    while d != s and d in parent.keys():
        d = parent[d]
        path.append(d)

    path.reverse()

    if path:
        path.append(des)
        return path
    else:
        return None


def edmonds_karp(graph, s, d):
    max_flow = 0

    while True:
        path = path_between(graph, s, d)
        if not path:
            break

        edges_on_path = list(zip(path[:-1], path[1:]))
        val = []
        for edge in edges_on_path:
            val.append(graph.edges[edge[0], edge[1]]["capacity"])

        min_flow_in_single_path = min(val)
        max_flow += min_flow_in_single_path

        for edge in edges_on_path:
            cap = graph.edges[edge[0], edge[1]]["capacity"]
            cap -= min_flow_in_single_path
            graph.remove_edge(edge[0], edge[1])

            return_cap = 0
            if graph.has_edge(edge[1], edge[0]):
                return_cap = graph.edges[edge[1], edge[0]]["capacity"]
                graph.remove_edge(edge[1], edge[0])
            return_cap += min_flow_in_single_path
            graph.add_edge(edge[1], edge[0], capacity=return_cap)

            if cap != 0:
                graph.add_edge(edge[0], edge[1], capacity=cap)

    return max_flow


'''wybór pliku z kótrego graf będzię wczytany '''
file = open('adj_list.txt', 'r')

source, destination = map(int, file.readline().split())

'''Jeśli graf jest w postaci listy sąsiedztwa  wybierz graph_from_adjacency_list,
 jeśli graf jest w postaci listy krawędzi  wybierz raph_from_list_of_edges'''

g = graph_from_adjacency_list(file)
# g = graph_from_list_of_edges(file)

'''wypisuje najwiekszy przepływ na podstawie algorytmu edmondsa-karpa'''
print(edmonds_karp(g, source, destination))

file.close()
