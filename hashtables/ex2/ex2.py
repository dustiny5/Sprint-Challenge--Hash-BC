#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for tic in tickets:
        hash_table_insert(hashtable, tic.source, tic.destination)
      
    retrieve = hash_table_retrieve(hashtable, 'NONE')
    k = 0
    while k < length:
        route[k] =  retrieve
        retrieve = hash_table_retrieve(hashtable, retrieve)
        k += 1

    return route
