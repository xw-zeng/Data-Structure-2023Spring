import numpy as np


def find_queen(board, start=0):
    # board是N*N的棋盘，0表示可放置的格子，1表示放置了皇后棋子的格子
    # start表示从第几行开始搜索放置皇后的位置

    def check_queen(i, j):  # 检查第i,j个格子是否可放置皇后
        if (board[i, :] == 1).any() | (board[:, j] == 1).any():  # 检查所在行和列是否有皇后
            return False
        for p, q in zip(list(range(i - 1, -1, -1)), list(range(j - 1, -1, -1))):  # 检查左上角是否有皇后
            if board[p, q] == 1:
                return False
        for p, q in zip(list(range(i - 1, -1, -1)), list(range(j + 1, N))):  # 检查右上角是否有皇后
            if board[p, q] == 1:
                return False
        # 不用检查下方是否有皇后是因为算法是从上到下开始放的
        return True

    def show_board(board):  # 显示棋盘和皇后所在位置
        for i in board:
            for j in i:
                if j == 1:
                    print('♚ ', end='')
                else:
                    print('□ ', end='')
            print('\n', end='')
        print('')

    if start > N - 1:  # 超出棋盘范围后停止递归（基本情况）
        global count
        count += 1  # 解的数量加1
        show_board(board)
    else:
        for j in range(N):
            if check_queen(start, j):
                board[start, j] = 1  # 假设在当前位置放置皇后
                find_queen(board, start + 1)  # 每行只能放置一个皇后，因此直接到下一行搜索放置皇后的位置
                board[start, j] = 0  # 撤销对棋盘的上一步操作


N = 8
board = np.zeros((N, N), dtype = int)
count = 0
find_queen(board)
print(f'{N}x{N}的国际象棋棋盘上共有{count}种符合条件的{N}个皇后的放置方法。')
