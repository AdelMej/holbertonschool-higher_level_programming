#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = (len(sentence), None if sentence == "" else sentence[0])
    return new_tuple
