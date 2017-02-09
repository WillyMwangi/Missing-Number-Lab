"""
MISSING NUMBER LAB
  You are presented with two arrays, all containing positive integers.
  One of the arrays will have one extra number.
  -->[1,2,3] and [1,2,3,4] should return 4
  -->[4,66,7] and [66,77,7,4] should return 77
"""


def find_missing(List1, List2): # This function compares two lists and returns the extra number in the longer list
    biggerList = []
    shorterList = []
    if len(List1) > len(List2):
        biggerList = List1
        shorterList = List2
    else:
        biggerList = List2
        shorterList = List1
    addedNumber = [x for x in biggerList if x not in shorterList]
    if len(addedNumber) == 0:
        return 0
    return addedNumber.pop()