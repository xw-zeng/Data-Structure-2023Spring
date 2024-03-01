import time


def add_numbers(ls):
    total = 0
    for v in ls:
        total = total + v
    return total


start = time.time()
add_numbers(range(1, 1000001))
end = time.time()
print(f'计算需要约{round((end - start) * 1000, 6)}毫秒。')
