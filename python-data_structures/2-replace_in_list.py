from typing import List, Any


def replace_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position.

    Args:
        my_list (list): The list to modify.
        idx (int): The index at which to replace the element.
        element: The new element to insert.

    Returns:
        list: The modified list with the element replaced if idx is valid,
              otherwise the original list.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    my_list[idx] = element
    return my_list
