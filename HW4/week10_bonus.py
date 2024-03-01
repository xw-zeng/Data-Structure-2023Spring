from graph import Graph


def MST_Boruvka(g):
    """Compute a minimum spanning tree of weighted graph g with Boruvka Algorithm.
    Return a list of edges that comprise the MST."""
    C = [{v} for v in g.vertices()]
    V = set(g.vertices())
    tree = []
    n = g.vertex_count()
    while len(tree) < n - 1:
        for idx1, Ci in enumerate(C):
            min_weight = float('inf')
            min_edge = None
            for u in Ci:
                for v in (V - Ci):
                    if g.get_edge(u, v) is not None:
                        if g.get_edge(u, v).element() < min_weight:
                            min_weight = g.get_edge(u, v).element()
                            min_edge = g.get_edge(u, v)
                            min_opposite = v
            if min_edge:
                tree.append(min_edge)
                for idx2, other in enumerate(C):
                    if min_opposite in other:
                        C[idx1] |= other
                        C[idx2] = {}
                        break
        while {} in C:
            C.remove({})
    return tree


def graph_from_edgelist(E, directed=False):
    """Make a graph instance based on a sequence of edge tuples."""
    g = Graph(directed)
    V = set()
    for e in E:
        V.add(e[0])
        V.add(e[1])
    verts = {}
    for v in V:
        verts[v] = g.insert_vertex(v)
    for e in E:
        src = e[0]
        dest = e[1]
        element = e[2] if len(e) > 2 else None
        g.insert_edge(verts[src], verts[dest], element)
    return g


def graph():
    """Return a weighted, undirected graph. """
    E = (
        ('A', 'B', 2), ('A', 'C', 8), ('A', 'E', 7), ('B', 'C', 5), ('C', 'E', 8), 
        ('B', 'D', 7), ('C', 'D', 9), ('E', 'F', 3), ('D', 'F', 4)
    )
    return graph_from_edgelist(E, False)


def display_tree(tree, directed=False):
    print('| ', end='')
    if directed:
        for e in tree:
            print(f'{e.endpoints()[0].element()}->{e.endpoints()[1].element()}', end=' | ')
    else:
        for e in tree:
            print(f'{e.endpoints()[0].element()}<->{e.endpoints()[1].element()}', end=' | ')
    print('\n')


g = graph()
tree = MST_Boruvka(g)
display_tree(tree)
