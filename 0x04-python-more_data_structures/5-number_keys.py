#!/usr/bin/python3
def number_keys(a_dictionary):
    num_key = 0
    for k, v in a_dictionary.items():
        num_key += 1
    return num_key
