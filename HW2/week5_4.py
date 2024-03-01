# 定义Empty异常类。
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


# 定义链表LinkedList类，该类含有头节点（哨兵节点），且只定义了以下在本题中需要用到的函数：
# is_empty: 检查链表是否为空。
# first: 返回头部元素的值。
# remove_first: 在头部删除元素。
# add_last: 在尾部添加元素。
# display: 可视化链表，便于查看结果。
class LinkedList:
    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # --------------------------- linked list methods ---------------------------
    def __init__(self):
        """Create an empty linked list."""
        self._head = self._Node(None, None)
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the linked list."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the head."""
        if self.is_empty():
            raise Empty('Linked list is empty.')
        return self._head._next._element

    def remove_first(self):
        """Remove an element at the head."""
        if self.is_empty():
            raise Empty('Linked list is empty.')
        self._head._next = self._head._next._next
        self._size -= 1

    def add_last(self, e):
        """Insert an element at the tail."""
        if self.is_empty():
            self._tail = self._Node(e, None)
            self._head._next = self._tail
        else:
            self._tail._next = self._Node(e, None)
            self._tail = self._tail._next
        self._size += 1

    def display(self):
        """Display all the elements in the linked list."""
        if self.is_empty():
            raise Empty('Linked list is empty.')
        else:
            x = []
            for i in range(self._size):
                x.append(str(self.first()))
                self.add_last(self.first())
                self.remove_first()
            print('->'.join(x))


# 定义输入有序列表输出有序单向链表的函数。
# 为避免用户输入的列表是乱序的，在数据结构转换前先对输入列表进行排序，以保证生成的单向链表是有序的。
def ordered_linkedlist(x: list) -> LinkedList:
    x = sorted(x)
    out = LinkedList()
    for i in x:
        out.add_last(i)
    return out


# 定义将两个有序的单向链表合并为一个有序链表，且合并后使原链表为空的函数。
def merge_linkedlist(a: LinkedList, b: LinkedList) -> LinkedList:
    # 创建新链表
    out = LinkedList()
    # 当单向链表a, b都非空时，比较a, b的头元素，将更小的元素加入新链表的尾部，然后在原链表中删除该头元素。
    while len(a) > 0 and len(b) > 0:
        if a.first() <= b.first():
            out.add_last(a.first())
            a.remove_first()
        else:
            out.add_last(b.first())
            b.remove_first()
    # 当a, b至少有一个为空时：
    # 将非空的单向链表中的头元素添加到新链表的尾部，在原链表中删除该头元素。
    # 循环上一步直至该单向链表为空。
    while len(a) > 0:
        out.add_last(a.first())
        a.remove_first()
    while len(b) > 0:
        out.add_last(b.first())
        b.remove_first()
    return out


# 测试
if __name__ == '__main__':
    # 将列表转换为有序的单向链表A, B
    A = ordered_linkedlist([2, 6, 4, 7, 0])
    B = ordered_linkedlist([5, 2, 3, 1, 9, 8, 6])
    # 展示单向链表A, B
    A.display(), B.display()
    # 将有序的单向链表A, B合并为新的有序链表AB_merged
    AB_merged = merge_linkedlist(A, B)
    # 展示合并后的有序链表AB_merged
    AB_merged.display()
    # 检查合并后原链表A, B是否都为空
    print(A.is_empty(), B.is_empty())
