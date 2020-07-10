def intersection(arrays):
    # number of inner arrays
    num_of_arrays = len(arrays)

    # keep track of unique integers with a tally / total of times we've seen them
    num_cache = {}

    # iterate through our array
    for inner_array in arrays:
        # iterate through each inner array and add to our num_cache
        for num in inner_array:
            if num not in num_cache:
                num_cache[num] = 1
            # if we have the number in our cache, increment its tally
            else:
                num_cache[num] += 1

    result = []

    # iterate through our num_cache and append any integers that have
    # an equal amount of instances to our number of inner arrays
    # to our final output
    for pair in num_cache.items():
        if pair[1] == num_of_arrays:
            result.append(pair[0])
    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
