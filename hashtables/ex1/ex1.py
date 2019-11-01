#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for index in range(length):
        hash_table_insert(ht, weights[index], index)

    if length < 2:
        return None
    elif length == 2:
        for lp in ht.storage:
            if lp:
                low = min(lp.next.value, lp.value)
                high = max(lp.next.value, lp.value)
                return (high, low)
                

    for weight in weights:
        weight_2 = limit - weight
        if weight_2 in weights and weight_2 > weight:
            return (hash_table_retrieve(ht, weight_2), hash_table_retrieve(ht, weight))
        elif weight_2 in weights and weight_2 < weight:
            return (hash_table_retrieve(ht, weight_2), hash_table_retrieve(ht, weight))

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
