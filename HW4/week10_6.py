from graph import Graph  # Source Code/Ch14/graph.py


class MyGraph(Graph):
    def remove_vertex(self, v):
        """Remove the Vertex v."""
        self._validate_vertex(v)
        # 删除所有与顶点v相连的边
        edges = self._outgoing.pop(v, None)
        if edges:
            for e in edges.values():
                e._origin = None
                e._destination = None
        for _, v_dict in self._outgoing.items():
            e = v_dict.pop(v, None)
            if e:
                e._origin = None
                e._destination = None
        edges = self._incoming.pop(v, None)
        if edges:
            for e in edges.values():
                e._origin = None
                e._destination = None
        for _, u_dict in self._incoming.items():
            e = u_dict.pop(v, None)
            if e:
                e._origin = None
                e._destination = None

    def remove_edge(self, e):
        """Remove the Edge e."""
        u, v = e.endpoints()
        if (u is not None) & (v is not None):
            del self._outgoing[u][v]
            del self._incoming[v][u]
            # 将被删除边的起点和终点修改为None，以说明该边已被删除
            e._origin = None
            e._destination = None
        else:
            print('This edge has already been removed.')


def graph_from_edgelist(E, directed=False):
    """Make a graph instance based on a sequence of edge tuples."""
    g = MyGraph(directed)
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


def display_graph(g):
    """Return all vertices and edges in the graph."""
    v_list = list(g.vertices())
    for v in v_list:
        print(v, end=' ')
    print('| ', end='')
    if g.is_directed():
        for key1, value1 in g._outgoing.items():
            for key2, _ in value1.items():
                print(f'{key1.element()}->{key2.element()}', end=' | ')
    else:
        e_list = list(g.edges())
        for e in e_list:
            print(f'{e._origin.element()}<->{e._destination.element()}', end=' | ')
    print('\n')


def graph(directed):
    """Return an unweighted graph. """
    E = (
        ('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D'),
        ('D', 'E'), ('E', 'F'), ('D', 'F'),
    )
    return graph_from_edgelist(E, directed)


if __name__ == '__main__':
    # 无向图
    g1 = graph(False)
    print('[无向图]', '节点数:', g1.vertex_count(), '边数:', g1.edge_count())
    display_graph(g1)
    # 删除一个节点
    v1 = list(g1.vertices())[0]
    g1.remove_vertex(v1)
    print('[无向图]', '删除的节点为:', v1, ', 剩余边数:', g1.edge_count())
    display_graph(g1)
    # 删除一条边
    e1 = list(g1.edges())[0]
    print('[无向图]', f'删除的边为: {e1._origin}<->{e1._destination}', end='')
    g1.remove_edge(e1)
    print(', 剩余边数:', g1.edge_count())
    display_graph(g1)
    # 有向图
    g2 = graph(True)
    print('[有向图]', '节点数:', g2.vertex_count(), '边数:', g2.edge_count())
    display_graph(g2)
    # 删除一个节点
    v2 = list(g2.vertices())[1]
    g2.remove_vertex(v2)
    print('[有向图]', '删除的节点为:', v2, ', 剩余边数:', g2.edge_count())
    display_graph(g2)
    # 删除一条边
    e2 = list(g2.edges())[1]
    print('[有向图]', f'删除的边为: {e2._origin}->{e2._destination}', end='')
    g2.remove_edge(e2)
    print(', 剩余边数:', g2.edge_count())
    display_graph(g2)
