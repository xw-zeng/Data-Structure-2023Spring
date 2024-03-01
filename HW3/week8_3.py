from heap_priority_queue import HeapPriorityQueue

from heap_priority_queue import HeapPriorityQueue


class MyHeapPriorityQueue(HeapPriorityQueue):

    def _upheap(self, j):
        """重写向上冒泡方法"""
        while j > 0 and self._data[j] < self._data[self._parent(j)]:  # 当这个元素不在堆顶，且比父节点小时，向上冒泡
            self._swap(j, self._parent(j))  # 交换它和它的父节点
            j = self._parent(j)  # 将j更新为它的父节点

    def _downheap(self, j):
        """重写向下冒泡方法"""
        while self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:  # 如果这个节点的最小的孩子比自己小，就向下冒泡
                self._swap(j, small_child)  # 交换它和它的最小的孩子节点
            j = small_child  # 将j更新为它的最小的孩子节点


def construct_heap(heap):
    """根据课件上的堆加入元组"""
    heap.add(4, 'C')
    heap.add(5, 'A')
    heap.add(6, 'Z')
    heap.add(15, 'K')
    heap.add(9, 'F')
    heap.add(7, 'Q')
    heap.add(20, 'B')
    heap.add(16, 'X')
    heap.add(25, 'J')
    heap.add(14, 'E')
    heap.add(12, 'H')
    heap.add(11, 'S')
    heap.add(13, 'W')


# 测试
if __name__ == '__main__':
    # 建立Source Code中的递归冒泡堆
    heap = HeapPriorityQueue()
    construct_heap(heap)
    # 建立自己写的非递归冒泡堆
    my_heap = HeapPriorityQueue()
    construct_heap(my_heap)
    print('基于数组表示的堆:\n', my_heap._data, '\n')
    print('向上冒泡：')
    # 增加元组(2,'T')
    heap.add(2, 'T')
    my_heap.add(2, 'T')
    print('- 递归：\n', heap._data)
    print('- 非递归：\n', my_heap._data, '\n')
    # 移除最小元组
    print('向下冒泡：')
    heap.remove_min()
    my_heap.remove_min()
    print('- 递归：\n', heap._data)
    print('- 非递归：\n', my_heap._data)
