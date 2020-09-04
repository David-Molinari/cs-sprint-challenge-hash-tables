#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    links = {}
    counter = 0
    for i in tickets:
        links[i.source] = i.destination
    route.append(links["NONE"])
    while counter < length - 1:
        route.append(links[route[counter]])
        counter += 1
    return route
