def has_negatives(a):
    cache = {}

    for num in a:
        num = abs(num)

        if num not in cache:
            cache[num] = 1
        else:
            cache[num] += 1


    key = list(cache.items())
    result = []
    for i in key:
        if i[1] > 1:
            result.append(i[0])
        else:
            continue

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
