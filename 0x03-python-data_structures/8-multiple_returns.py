#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        mul_tuple = (0, None)
        return mul_tuple
    else:
        mul_tuple = (len(sentence), sentence[0])
        return mul_tuple
