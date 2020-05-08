#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtable import HashTable

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}

    for i in tickets:
        cache[i.source] = (i.destination)

    route = []
    current = cache["NONE"]
    route.append(current)

    for i in range(1, length):
        next_stop = cache[current]
        route.append(next_stop)
        current = next_stop



    return route

