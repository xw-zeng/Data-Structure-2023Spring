
import ctypes  # provides low-level arrays


# 定义Empty异常类。
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


# 自定义基于列表的动态数组类DynamicArray
# 在Source Code/Ch05/dynamic_array.py的基础上新添加了`is_empty`、`locate`、`delete`方法
class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def is_empty(self):
        """Return True if the array is empty."""
        return self._n == 0

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]  # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):  # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
        self._A = B  # use the bigger array
        self._capacity = c

    def _make_array(self, c):  # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()  # see ctypes documentation

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        for j in range(self._n, k, -1):  # shift rightmost first
            self._A[j] = self._A[j - 1]
        self._A[k] = value  # store newest element
        self._n += 1

    def delete(self, k):
        """Delete value at index k, shifting subsequent values leftward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        # note: we do not consider shrinking the dynamic array in this version
        for j in range(k, self._n - 1):  # shift leftward
            self._A[j] = self._A[j + 1]
        self._A[self._n - 1] = None  # help garbage collection
        self._n -= 1  # we have one less item

    def locate(self, value):
        """Return the index of first occurrence of value (or raise ValueError)."""
        for k in range(self._n):
            if self._A[k] == value:  # found a match!
                return k
        raise ValueError('value not found')  # only reached if no match

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:  # found a match!
                for j in range(k, self._n - 1):  # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None  # help garbage collection
                self._n -= 1  # we have one less item
                return  # exit immediately
        raise ValueError('value not found')  # only reached if no match


# 定义基于数组的双端队列类，继承DynamicArray数组类。
class ArrayDeque(DynamicArray):

    def __init__(self, D0=None):
        """Initialize the deque using D0."""
        # note: we do not consider other data types of D0 except Nonetype, DynamicArray, ArrayDeque and list
        super().__init__()  # use inherited construction method
        if type(D0) == DynamicArray or type(D0) == ArrayDeque:
            self._resize(D0._capacity)
            self._A = D0._A
            self._n = D0._n
        if type(D0) == list:
            self._resize(len(D0))
            for value in D0:
                self.append(value)

    # 这里可以不用重写，因为其父类已经写好了这个方法，重新写只是为了说明该类的完整性
    def __len__(self):
        """Return the number of elements in the deque."""
        return self._n

    # 这里可以不用重写，因为其父类已经写好了这个方法，重新写只是为了说明该类的完整性
    def is_empty(self):
        """Return True if the deque is empty."""
        return self._n == 0

    def add_first(self, e):
        """Add an element to the front of the deque."""
        self.insert(0, e)

    def add_last(self, e):
        """Add an element to the back of the deque."""
        self.append(e)

    def delete_first(self):
        """Remove and return the element from the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty.")
        value = self._A[0]
        self.delete(0)
        return value

    def delete_last(self):
        """Remove and return the element from the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty.")
        value = self._A[self._n - 1]
        self.delete(self._n - 1)
        return value

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._A[0]

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._A[self._n - 1]

    def clear(self):
        """Remove all elements from the deque."""
        if self.is_empty():
            raise Empty("Deque is empty.")
        while self._n != 0:
            self.delete_last()


# 测试（最好一行一行跑，否则只会输出最后的结果）
# example in "4. 数组、栈与队列（2）.pdf" Page 34
D = ArrayDeque()
D.add_last(5)
D.add_first(3)
D.add_first(7)
D.first()
D.delete_last()
len(D)
D.delete_last()
D.delete_last()
D.add_first(6)
D.last()
D.add_first(8)
D.is_empty()
D.last()
# test the init and clear function not present in instruction materials
D0 = [1, 2, 3, 4, 5]  # the type of D0 can also be DynamicArray or ArrayDeque
D = ArrayDeque(D0)  # Use D0 to initialize D
D.first()
D.delete_last()
len(D)
D.clear()
D.is_empty()  # check whether all the elements in the deque are deleted
