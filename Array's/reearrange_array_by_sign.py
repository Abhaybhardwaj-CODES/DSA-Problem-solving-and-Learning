def rearrange_by_sign(arr):
    n = len(arr)
    ans = [0] * n

    pos = 0
    neg = 1

    for num in arr:
        if num > 0:
            ans[pos] = num
            pos += 2
        else:
            ans[neg] = num
            neg += 2

    return ans


arr = [3, 1, -2, -5, 2, -4]

print(rearrange_by_sign(arr))