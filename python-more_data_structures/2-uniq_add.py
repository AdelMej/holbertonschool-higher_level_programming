#!/usr/bin/python3
def uniq_add(my_list=[]):
    occurence = []
    sum = 0
    for i in my_list:
        if i not in occurence:
            occurence.append(i)
            sum += i

    return sum
