def lazy_hanoi(N):

    def show_move(p, i, j):
        global count
        count += 1
        print(f'move({p}, {i}, {j})')

    if N == 1:
        show_move(N, 0, 2)
    else:
        for i in range(1, N):
            show_move(i, 0, 2 - (N - i) % 2)
            for j in range(1, i):
                show_move(j, 1 + (N - i) % 2, 2 - (N - i) % 2)
        show_move(N, 0, 2)
        for i in range(N - 1, 0, -1):
            for j in range(1, i):
                show_move(j, (N - i) % 2, 1 - (N - i) % 2)
            show_move(i, (N - i) % 2, 2)


N = 5
count = 0
lazy_hanoi(N)
print(f'在懒和尚问题中把{N}个金盘从柱子0移动到柱子2总共需要移动{count}次。')