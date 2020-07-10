def has_negatives(a):
    # cache to keep track of
    num_cache = {}

    # iterate through our list and add to our num_cache to keep track
    for i in a:
        if i not in num_cache:
            num_cache[i] = None

    result = []

    # iterate through our cache
    # if our key is positive and its negative counterpart is also in our
    # cache, then append it to our final result
    for pair in num_cache.items():
        if pair[0] > 0 and -pair[0] in num_cache:
            result.append(pair[0])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
