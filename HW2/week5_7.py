
from linked_binary_tree import LinkedBinaryTree # import from Source Code Ch08

class MyLinkedBinaryTree(LinkedBinaryTree):
  """Linked representation of a binary tree structure."""

  #-------------------------- binary tree constructor --------------------------
  def __init__(self):  # 重写父类的构造方法，取消_root，增加_sentinel哨兵节点
    """Create an initially empty binary tree."""
    self._sentinel = self._Node(None)  # 哨兵节点
    self._size = 0

  #-------------------------- public accessors --------------------------
  def root(self):  # 重写返回根节点的位置的方法
    """Return the root Position of the tree (or None if tree is empty)."""
    return self._make_position(self._sentinel._left)  # 根节点是哨兵节点的左孩子

  #-------------------------- nonpublic mutators --------------------------
  def _add_root(self, e):  # 重写添加根节点的方法
    """Place element e at the root of an empty tree and return new Position."""
    if self._sentinel._left is not None:  # 当根节点已经存在时报错
      raise ValueError('Root exists')
    self._size = 1
    self._sentinel._left = self._Node(e, self._sentinel)  # 令哨兵节点的左孩子指向新的节点，令新的节点的父节点指向哨兵节点
    return self._make_position(self._sentinel._left)  # 返回根节点的位置

  def _delete(self, p):  # 重写删除位置p节点的方法
    """Delete the node at Position p, and replace it with its child, if any."""
    node = self._validate(p)  # 将位置拆包为节点
    if self.num_children(p) == 2:  # 当该节点有两个孩子时报错
      raise ValueError('Position has two children')
    child = node._left if node._left else node._right  # 有可能为空
    if child is not None:
      child._parent = node._parent   # 让孩子节点的父亲变为它原来父节点的父节点
    parent = node._parent
    if node is parent._left:  # 让新的父节点指向孩子节点
      parent._left = child
    else:
      parent._right = child
    self._size -= 1
    node._parent = node  # 将该节点的父亲指向自己，便于内存回收
    return node._element
  
  def _attach(self, p, t1, t2):  # 重写为叶子节点连接子树的方法
    """Attach trees t1 and t2, respectively, as the left and right subtrees of the external Position p."""
    node = self._validate(p)  # 将位置拆包为节点
    if not self.is_leaf(p):  # 检查是否为叶子节点
      raise ValueError('position must be leaf')
    if not type(self) is type(t1) is type(t2):  # 检查三棵树的类型是否相同
      raise TypeError('Tree types must match')
    self._size += len(t1) + len(t2)
    if not t1.is_empty():                 # 连接t1左子树
      node._left = t1._sentinel._left     # 让该节点左边连接到t1的根节点
      t1._sentinel._left._parent = node   # 让t1的根节点的父亲变为该节点
      t1._sentinel = self._Node(None)     # 让t1实例变为空
      t1._size = 0
    if not t2.is_empty():                 # 连接t2右子树
      node._right = t2._sentinel._left    # 让该节点右边连接到t2的根节点
      t2._sentinel._left._parent = node   # 让t2的根节点的父亲变为该节点
      t2._sentinel = self._Node(None)     # 让t2实例变为空
      t2._size = 0


# 测试
T = MyLinkedBinaryTree()
T._add_root(1)
n1 = T._add_left(T.root(), 2)
len(T)
n2 = T._add_left(n1, 3)
n3 = T._add_right(n1, 4)
T.depth(n3)
T.height(n1)
T._delete(T.root())  # 删除根节点
T.root() == n1  # 检查根节点是否变为原根节点的左孩子n1
