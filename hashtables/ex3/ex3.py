def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    array_counter = len(arrays)
    duplicates_tracker = {}
    result = []
    for i in arrays:
        for e in i:
            found = duplicates_tracker.get(e)
            if found != None:
                duplicates_tracker[e] += 1
                if duplicates_tracker[e] == array_counter:
                    result.append(e)
            else:
                duplicates_tracker[e] = 1
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
