from mst import MST_Kruskal
from graph import Graph


class Partition:
    """Union-find structure for maintaining disjoint sets."""

    def __init__(self):
        self.group = []

    # ------------------------- nested Position class -------------------------
    class Position:
        __slots__ = '_container', '_element'

        def __init__(self, container, e):
            """Create a new position that is the leader of its own group."""
            self._container = container  # reference to Partition instance
            self._element = e

        def element(self):
            """Return element stored at this position."""
            return self._element

    # ------------------------- nonpublic utility -------------------------
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')

    # ------------------------- public Partition methods -------------------------
    def make_group(self, e):
        """Makes a new group containing element e, and returns its Position."""
        self.group.append({e})
        return self.Position(self, e)

    def find(self, p):
        """Finds the group containging p and return this group."""
        self._validate(p)
        for s in self.group:
            if p.element() in s:
                return s
        raise ValueError('p does not belong to this container')

    def union(self, p, q):
        """Merges the groups p and q (if distinct)."""
        if p is not q:  # only merge if different groups
            p |= q
            self.group.remove(q)


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
        ('0', '1', 2.24), ('0', '3', 2.24), ('0', '4', 4.47), ('1', '5', 3.61), ('2', '4', 3.61),
        ('2', '3', 3.16), ('2', '5', 2.24), ('3', '4', 3), ('3', '5', 2.24)
    )
    return graph_from_edgelist(E, False)


def display_tree(tree, directed=False):
    print('| ', end='')
    if directed:
        for e in tree:
            print(
                f'{e.endpoints()[0].element()}->{e.endpoints()[1].element()}', end=' | ')
    else:
        for e in tree:
            print(
                f'{e.endpoints()[0].element()}<->{e.endpoints()[1].element()}', end=' | ')
    print('\n')


g = graph()
tree = MST_Kruskal(g)
display_tree(tree)
