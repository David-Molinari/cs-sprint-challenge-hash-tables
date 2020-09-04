def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dictionary0 ={}
    counter = 0
    answer = ()
    for w in weights:
        found = dictionary0.get(limit - w)
        if found != None:
            answer = (counter, found)
            return answer
        dictionary0[w] = counter
        counter += 1
    return None
