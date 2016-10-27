if __name__ == "__main__":
    a = [11, -8, 16, -7, 24, -2, 3]
    k = 3
    i = 0
    j = i + k - 1
    size = len(a)
    max_sum = 0
    for t in range(i, j + 1):
        max_sum += a[t]
    temp = max_sum
    while (j < size - 1):

        j += 1
        temp += a[j]
        print a[j], a[i]
        temp -= a[i]
        i += 1
        if temp > max_sum:
            max_sum = temp
    print max_sum, float(max_sum) / k
