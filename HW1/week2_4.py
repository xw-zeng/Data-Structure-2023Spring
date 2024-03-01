class ArrayStack:  # 基于list类实现栈类

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


def solve_hanoi(tower, N, x=0, m=1, y=2):  # 把N个盘子从柱子0移动到柱子2

    def move(i, j):  # 从柱子i移动一个盘子到柱子j
        global count
        count += 1
        p = tower[i].pop()
        tower[j].push(p)
        print(f'move({p}, {i}, {j})')

    if N == 1:
        move(x, y)
    else:
        solve_hanoi(tower, N - 1, x, y, m)  # 把N-1个盘子从柱子0移动到柱子1
        move(x, y)
        solve_hanoi(tower, N - 1, m, x, y)  # 把N-1个盘子从柱子1移动到柱子2


N = 3 # 指定盘子数N
tower = [ArrayStack(), ArrayStack(), ArrayStack()] # 定义3根柱子0、1、2
for i in range(N, 0, -1): # 向柱子0从大到小压入N个盘子
    tower[0].push(i)

count = 0
solve_hanoi(tower, N)
print(f'把{N}个金盘从柱子0移动到柱子2总共需要移动{count}次。')
