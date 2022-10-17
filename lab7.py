#########################
# EECS1015 - York University
# Lab #7 - Starting Code
#  Writing test cases
#  Make sure you install PyTest (see lecture notes)
#  NOTE - You can only run this in PyCharm for a project that has installed PyTest
#  You cannot double click on this file.  That is fine, we can test it once you submit it.
#########################

import pytest
from typing import List

# Accepts a list of integers
def initializeMinMaxList(myList: List[int]) -> None:   # given
    myList.sort()


def insertItem(myList: List[int], item: int) -> None:  # given
    myList.append(item)
    myList.sort()

def getMinMax(myList: List[int], minormax: str) -> int:   # given -- but requires additional assert
    assert minormax.upper()=="MAX" or minormax.upper()=="MIN", "2nd argument must be 'Min' or 'Max' "
    assert len(myList) != 0, "List must not be empty"
    result: int
    if minormax == "MAX":
        result = myList[-1]
        del myList[-1]
    else:
        result = myList[0]
        del myList[0]
    return result

# Main function is given.
def main():
    aList = [10, 11, 99, 1, 55, 100, 34, 88]
    print("Starting List: ", aList)
    initializeMinMaxList(aList)

    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("Insert %d %d %d %d" % (min1 - 1, min2 - 1, max1 + 1, max2 + 1))
    insertItem(aList, min1 - 1)
    insertItem(aList, min2 - 1)
    insertItem(aList, max1 + 1)
    insertItem(aList, max2 + 1)

    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("DONE.  Type Enter to exit.")
    input()


if __name__ == "__main__":
    main()


#####
# WRITE YOUR TEST CASES BELOW HERE
#
######

# Lab 7
# Author: Ravish Kamath
# Email: ravish96@my.yorku.ca
# Student ID: 213893664

def test_getMinMaxCase1():
    x = [420,69]
    initializeMinMaxList(x)
    minX = getMinMax(x, "MIN")
    assert minX == 69, "Min should be 69"
    maxX = getMinMax(x, "MAX")
    assert maxX == 420, "Max should be 420"


def test_getMinMaxCase2():
    y = [2307]
    initializeMinMaxList(y)
    minY = getMinMax(y, "MIN")
    assert minY == 2307, "Min should be 2307"
    insertItem(y, minY)
    maxY = getMinMax(y, "MAX")
    assert maxY == 2307, "Max should be 2307"


def test_getMinMaxCase3():
    z = []
    initializeMinMaxList(z)
    insertItem(z, 1959)
    insertItem(z, 4013597)
    minZ = getMinMax(z, "MIN")
    assert minZ == 1959, "Min should be 1959"
    maxZ = getMinMax(z, "MAX")
    assert maxZ == 4013597, "Max should be 4013597"


def test_getMinMaxRequestError():
    x = [10, 20, 2]
    initializeMinMaxList(x)
    with pytest.raises(AssertionError) as e:
        minMaxX = getMinMax(x, "MID")
    assert e.typename == "AssertionError", "Should raise AssertionError!"


def test_getMinMaxEmptyError():
    x = []
    initializeMinMaxList(x)
    with pytest.raises(AssertionError) as e:
        result = getMinMax(x,"MIN")
        assert len(x) != 0, "list must not be empty"
    with pytest.raises(AssertionError) as e2:
        result = getMinMax(x, "MAX")
        assert len(x) != 0, "list must not be empty"
    assert e.typename == "AssertionError", "Should raise AssertionError"
    assert e2.typename == "AssertionError", "Should raise AssertionError"
