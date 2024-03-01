import numpy as np


def sort_list(x):
    # 向上冒泡
    def upheap(x, bound):
        j = bound - 1
        while j > 0 and x[j] > x[(j - 1) // 2]:  # 当这个元素不在堆顶，且比父节点大时，向上冒泡
            x[j], x[(j - 1) // 2] = x[(j - 1) // 2], x[j]  # 交换它和它的父节点
            j = (j - 1) // 2  # 将j更新为它的父节点

    # 向下冒泡
    def downheap(x, bound):
        j = 0
        while 2 * j + 1 < bound - 1:  # 有左孩子
            left = 2 * j + 1
            big_child = left
            if 2 * j + 2 < bound - 1:  # 有右孩子
                right = 2 * j + 2
                if x[right] > x[left]:  # 选择左右孩子中最大的一个孩子
                    big_child = right
            if x[big_child] > x[j]:  # 当大孩子比这个元素大时，向下冒泡
                x[j], x[big_child] = x[big_child], x[j]  # 交换它和大孩子节点
            j = big_child  # 将j更新为大孩子节点

    # 第一阶段
    for bound in range(len(x) + 1):  # bound表示堆与序列的分界线，即序列开头的index
        upheap(x, bound)

    # 第二阶段
    for bound in range(len(x))[::-1]:
        x[0], x[bound] = x[bound], x[0]
        downheap(x, bound + 1)

    return x


# 测试
if __name__ == '__main__':
    x = np.random.randint(0, 20, 20)
    print(sort_list(x))
