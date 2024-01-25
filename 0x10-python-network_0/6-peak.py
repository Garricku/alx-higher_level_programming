#!/usr/bin/python3
"""Defines the module 6-peak"""


def find_peak(list_of_integers):
    """Defines a method that finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) >= 2:
        peak = max(list_of_integers)
    return peak
