from probe_hash_map import ProbeHashMap


class MyProbeHashMap(ProbeHashMap):

    def _hash_function(self, k):
        """重写哈希函数，修改为更简单的模运算"""
        return k % len(self._table)

    def __setitem__(self, k, v):
        """重写__setitem__方法，减少了resize步骤"""
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)

    def _set_probe(self, method):
        """设置探测方法，包含线性探测法和二次探测法"""
        self.probe = 2 if method == 'quadratic' else 1  # 表示f(i)中i的次数

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j."""
        firstAvail = None
        i = 0  # 计数探测了几次
        idx = j  # 记录原来的hash值
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False, firstAvail)
            elif k == self._table[j]._key:
                return (True, j)
            i += 1
            j = (idx + i ** self.probe) % len(self._table)


def construct_hash_map(cap, method):
    hash_map = MyProbeHashMap(cap=cap)
    hash_map._set_probe(method)
    hash_map[18] = 'A'
    hash_map[41] = 'B'
    hash_map[22] = 'C'
    hash_map[44] = 'D'
    hash_map[59] = 'E'
    hash_map[32] = 'F'
    hash_map[31] = 'G'
    hash_map[73] = 'H'
    return hash_map


# 测试
if __name__ == '__main__':
    hash_map1 = construct_hash_map(13, 'linear')
    hash_map2 = construct_hash_map(13, 'quadratic')
    print('一次探测法：', end='')
    for i in iter(hash_map1):
        print(i, end=' ')
    print('\n二次探测法：', end='')
    for i in iter(hash_map2):
        print(i, end=' ')
