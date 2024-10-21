"""Exercise Set 2: Data Structures"""

import numpy as np
import matplotlib as plt

# ex1
def exercise1(list1, list2):
    if not(isinstance(list1, list) and isinstance(list2, list)):
        raise Exception("One or both inserted objects are not lists!")

    if not(all(isinstance(elem, int) for elem in list1) and all(isinstance(elem, int) for elem in list2)):
        raise Exception("One or both lists contain non-integer characters!")

    if not(len(list1) > 0 and len(list2) > 1):
        raise Exception("One or both lengths of the lists are not valid!")

    list1_odd = [list1[idx] for idx, _ in enumerate(list1) if idx % 2 != 0]
    list1_even = [list2[idx] for idx, _ in enumerate(list2) if idx % 2 == 0]

    new_list = list1_odd + list1_even

    return new_list


# ex2
def exercise2():
    pass


# ex3
def exercise3():
    pass


# ex4
def exercise4():
    pass


# ex5
def exercise5():
    pass


# ex6
def exercise6():
    pass


# ex7
def exercise7():
    pass


# ex8
def exercise8():
    pass


# ex9
def exercise9():
    pass


# ex10
def exercise10():
    pass


if __name__ == "__main__":
    print("EXERCISE SET 2: Data Structures")
    print("EX1")
    listOne = [3, 6, 9, 12, 15, 18, 21, 8]
    listTwo = [4, 8, 12, 16, 20, 24, 28]
    merged_list = exercise1(listOne, listTwo)
    print(f"The new list is:\n{merged_list}")

    print("EX2")
    exercise2()

    print("EX3")
    exercise3()

    print("EX4")
    exercise4()

    print("EX5")
    exercise5()

    print("EX6")
    exercise6()

    print("EX7")
    exercise7()

    print("EX8")
    exercise8()

    print("EX9")
    exercise9()

    print("EX10")
    exercise10()
