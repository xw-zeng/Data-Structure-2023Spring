
from week5_7 import MyLinkedBinaryTree  # import from week5_7


class MyBinarySearchTree(MyLinkedBinaryTree):  # 继承第7题写的MyLinkedBinaryTree类，有哨兵节点
  """Linked representation of a binary search tree structure."""

  def __init__(self, n, numbers):
    """Construct a binary search tree with a list of numbers."""
    super().__init__()
    if n == 0 or len(numbers) == 0 or n != len(numbers):  # 参数长度不符合，报错
      raise ValueError('Invalid parameters')
    self._add_root(numbers[0])  # 插入根节点
    for i in range(1, n):  # 按照numbers的顺序依次将节点加入树
      tmp = self.root()
      while True:
        if self.num_children(tmp) == 0:  # 如果节点的度为0，说明该节点为叶子节点，只需要判断大小直接插入即可
          if numbers[i] < tmp.element():
            self._add_left(tmp, numbers[i])
          else:
            self._add_right(tmp, numbers[i])
          break
        elif self.num_children(tmp) == 1:  # 如果节点的度为1，需要做判断
          if not self.left(tmp) and numbers[i] < tmp.element():
            self._add_left(tmp, numbers[i])
            break
          elif not self.right(tmp) and numbers[i] >= tmp.element():
            self._add_right(tmp, numbers[i])
            break
          elif numbers[i] < tmp.element():
            tmp = self.left(tmp)
          else:
            tmp = self.right(tmp)
        elif self.num_children(tmp) == 2:  # 如果节点的度为2，则判断大小转入其孩子节点进行循环
          if numbers[i] < tmp.element():
            tmp = self.left(tmp)
          else:
            tmp = self.right(tmp)
    self._complete()  # 将二叉树用井号补全

  #---------------------------- nested _Node class ----------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a node."""
    __slots__ = '_element', '_parent', '_left', '_right', '_subtreenodes'  # streamline memory usage

    def __init__(self, element, parent=None, left=None, right=None, subtreenodes=1):
      self._element = element
      self._parent = parent
      self._left = left
      self._right = right
      self._subtreenodes = subtreenodes  # 以该节点为根节点的子树的节点数量

  # -------------------------- nested Position class --------------------------
  class Position(MyLinkedBinaryTree.Position):
    """An abstraction representing the location of a single element."""

    def subtreenodes(self):
      """Return the number of children in the subtree whose root is at this Position."""
      return self._node._subtreenodes  # 返回以该节点为根节点的子树的节点数量

  #-------------------------- nonpublic mutators --------------------------
  def _add_root(self, e):  # 重写添加根节点的方法
    """Place element e at the root of an empty tree and return new Position."""
    if self._sentinel._left is not None:  # 当根节点已经存在时报错
      raise ValueError('Root exists')
    self._size = 1
    self._sentinel._left = self._Node(e, self._sentinel)  # 令哨兵节点的左孩子指向新的节点，令新的节点的父节点指向哨兵节点
    self._sentinel._subtreenodes = 2  # 为哨兵节点的该属性赋值为2
    return self._make_position(self._sentinel._left)  # 返回根节点的位置

  def _add_left(self, p, e, complete=False):
    """Create a new left child for Position p, storing element e."""
    node = self._validate(p)
    if node._left is not None:
      raise ValueError('Left child exists')
    node._left = self._Node(e, node)
    if not complete:
      self._size += 1
      node._subtreenodes += 1  # 该节点的孩子节点数+1
      tmp = node._parent
      while tmp is not None:  # 该节点的祖先节点的子树的孩子节点数+1
        tmp._subtreenodes += 1
        tmp = tmp._parent
    return self._make_position(node._left)

  def _add_right(self, p, e, complete=False):
    """Create a new right child for Position p, storing element e."""
    node = self._validate(p)
    if node._right is not None:
      raise ValueError('Right child exists')
    node._right = self._Node(e, node)
    if not complete:
      self._size += 1
      node._subtreenodes += 1  # 该节点的孩子节点数+1
      tmp = node._parent
      while tmp is not None:  # 该节点的祖先节点的子树的孩子节点数+1
        tmp._subtreenodes += 1
        tmp = tmp._parent
    return self._make_position(node._right)

  def _delete(self, p):  # 重写删除位置p节点的方法，因为删除节点后会对children的数量产生改变
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
    if child is not None:  # 将删除节点的孩子节点的所有祖先节点内记录的孩子数量-1
      tmp = child._parent
      while tmp is not None:
        tmp._subtreenodes -= 1
        tmp = tmp._parent
    self._size -= 1
    node._parent = node  # 将该节点的父亲指向自己，便于内存回收
    return node._element

  def _complete(self, fill='#'):
    positions = []
    for p in self.positions():
      positions.append(p)
    for p in positions:
      if self.num_children(p) != 2:
        if not self.left(p):
          self._add_left(p, fill, True)
        if not self.right(p):
          self._add_right(p, fill, True)

  def _subtree_search(self, p, e):
    """Return Position of p's subtree having value e, or last node searched."""
    if type(p.element()) == str:  # 如果位置p为井号字符串，则说明没有找到，返回None
      return None
    if e == p.element():  # 找到匹配的元素，返回对应的位置
      return p
    elif e < p.element():  # 查询左子树
      if self.left(p) is not None:
        return self._subtree_search(self.left(p), e)
    else:  # 查询右子树
      if self.right(p) is not None:
        return self._subtree_search(self.right(p), e)
    return None  # 没有找到，返回None

  #--------------------- public methods providing "positional" support ---------------------
  def display(self, method='preorder'):
    """Display all the elements stored in the tree in a given order, preorder, postorder or inorder."""
    if method == 'preorder':
      positions = self.preorder()
    elif method == 'postorder':
      positions = self.postorder()
    elif method == 'inorder':
      positions = self.inorder()
    for p in positions:
      print(p.element(), end=' ')
    print('\n', end='')

  def find_position(self, e):
    """Return position with value e, or None if empty."""
    if self.is_empty():
      return None
    else:
      p = self._subtree_search(self.root(), e)
      return p


# 测试
if __name__ == '__main__':
  n = int(input('请输入一个正整数n: \n'))  # 13
  numbers = input('\n请输入n个正整数，以空格隔开，代表存储在节点的关键字：\n').split()  # 10 4 11 2 6 12 13 1 3 5 8 7 9
  numbers = [int(number) for number in numbers]  # [10, 4, 11, 2, 6, 12, 13, 1, 3, 5, 8, 7, 9]
  BST = MyBinarySearchTree(n, numbers)
  print('\n前序遍历：')
  BST.display(method='preorder')
  print('\n中序遍历：')
  BST.display(method='inorder')
  print('\n后序遍历：')
  BST.display(method='postorder')
  print('\n____进入查询状态____')
  while True:
    value = input('\n请输入您想要查询其节点数目的子树的根节点的关键字: \n')
    if value.lower() == 'q':
      print('\n____结束查询____')
      break
    value = int(value)  # 转化为整数
    p = BST.find_position(value)
    if not p:
      print(0)
    else:
      print(p.subtreenodes())
