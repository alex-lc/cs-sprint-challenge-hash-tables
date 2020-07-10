class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # keep track of our routes in a cache
    routes = {}

    # iterate through our list of tickets and add any unknown routes to cache
    for route in tickets:
        if route not in routes:
            routes[route.source] = route.destination  

    # we know our starting source is any route that has a source of NONE
    start_source = routes['NONE']
    # final output list including our first source of NONE
    places = [start_source]

    # iterate over the length of our tickets list
    for x in range(length-1):
        next_source = places[x]
        # our next destination should be the value of the current source in our routes cache
        next_destination = routes[next_source]
        # add it to our final output of places to return
        places.append(next_destination)
    
    return places
