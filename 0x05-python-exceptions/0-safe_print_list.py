#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        printed_elements = 0
        for element in my_list[:x]:
            print(element, end="")
            printed_elements += 1
            print()
            return printed_element
        except Exception as e:
            return printed_elements
