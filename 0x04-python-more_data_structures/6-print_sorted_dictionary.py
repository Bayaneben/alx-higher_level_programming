#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in a_dictionary.keys():
        if type(key) != str :
            print('the key is not a string')
            exit()
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
