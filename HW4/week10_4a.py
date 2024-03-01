def my_inplace_quick_sort(S, a, b):
    if a >= b:
        return

    # 三位取中法
    mid = int(a + (b - a) / 2)
    left = a
    right = b
    if S[left] < S[mid]:
        if S[mid] < S[right]:
            pass
        else:  # S[mid] >= S[right]
            if S[left] > S[right]:
                S[left], S[mid], S[right] = S[right], S[left], S[mid]
            else:  # S[left] <= S[right]
                S[mid], S[right] = S[right], S[mid]
    else:  # S[left] >= S[mid]
        if S[mid] > S[right]:
            S[left], S[right] = S[right], S[left]
        else:  # S[mid] <= S[right]
            if S[left] > S[right]:
                S[left], S[mid], S[right] = S[mid], S[right], S[left]
            else:  # S[left] <= S[right]:
                S[left], S[mid] = S[mid], S[left]
    # if length of the list is 2 or 3, already sorted
    if b - a + 1 <= 3:
        return
    # if length of the list larger than 3
    pivot = S[mid]
    S[mid], S[right - 1] = S[right - 1], S[mid]  # swap the pivot with penultimate place
    right = b - 2

    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1

    # put pivot into its final place (currently marked by left index)
    S[left], S[b - 1] = S[b - 1], S[left]
    # make recursive calls
    my_inplace_quick_sort(S, a, left - 1)
    my_inplace_quick_sort(S, left + 1, b)


if __name__ == '__main__':
    s = [3, 1, 4, 7, 5, 2, 6, 8]
    my_inplace_quick_sort(s, 0, 7)
    print(s)
