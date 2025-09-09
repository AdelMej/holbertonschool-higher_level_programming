#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_elem = 0
    try:
        for i in range(x):
            print(my_list[i], end="" if i < x - 1 else "\n")
            nb_elem += 1
    except IndexError:
        print()
        return nb_elem

    return nb_elem
