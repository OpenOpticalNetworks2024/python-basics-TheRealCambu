"""Exercise Set 2: Data Structures"""

import numpy as np
import matplotlib as plt
import time


# ex1
def exercise1(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise Exception("One or both inserted objects are not lists!")

    if not (all(isinstance(elem, int) for elem in list1) and all(isinstance(elem, int) for elem in list2)):
        raise Exception("One or both lists contain non-integer characters!")

    if not (len(list1) > 0 and len(list2) > 1):
        raise Exception("One or both lengths of the lists are not valid!")

    list1_odd = [list1[idx] for idx, _ in enumerate(list1) if idx % 2 != 0]
    list1_even = [list2[idx] for idx, _ in enumerate(list2) if idx % 2 == 0]

    new_list = list1_odd + list1_even

    return new_list


# ex2
def exercise2(list1):
    if not isinstance(list1, list):
        raise Exception("The input onject is not a list!")

    if len(list1) < 2:
        raise Exception("The list should contain at least two elements!")

    second_elem = list1[3]
    new_list = list1.copy()
    new_list.remove(second_elem)
    first_part, second_part = new_list[0], new_list[1:]
    final_list = [first_part] + [second_elem] + second_part + [second_elem]

    print(f"The final list is:\n{final_list}")
    return final_list


# ex3
def exercise3(input_list):
    list1 = input_list[:3]
    list1.reverse()
    list2 = input_list[3:6]
    list2.reverse()
    list3 = input_list[6:]
    list3.reverse()

    print(f"The original list is: {input_list}\nThe new reverted list chunks are:\n"
          f"{list1}\n"
          f"{list2}\n"
          f"{list3}\n")


# ex4
def exercise4(input_list):
    if not isinstance(input_list, list):
        raise Exception("The input onject is not a list!")

    if not all(isinstance(elem, int) for elem in input_list):
        raise Exception("Not all the elements are non-negative integers!")

    if len(input_list) < 1:
        raise Exception("The list should contain at least two elements!")

    dictionary = {key: input_list.count(key) for key in set(input_list)}
    print(f"Dictionary to show the count for each element:\n{dictionary}")

    return dictionary


# ex5
def exercise5(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise Exception("The input onject is not a list!")

    if not (all(isinstance(elem, int) for elem in list1) and all(isinstance(elem, int) for elem in list2)):
        raise Exception("Not all the elements are non-negative integers!")

    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same size.")

    result_set = set(zip(list1, list2))
    print(f"Set to show the elements from both lists in the pair:\n{result_set}")

    return result_set


# ex6
def exercise6(set1, set2):
    if not (isinstance(set1, set) and isinstance(set2, set)):
        raise Exception("One or both input objects are not sets!")

    if not (len(set1) > 0 and len(set2) > 0):
        raise Exception("One or both sets are empty!")

    # Approach number 1
    new_set1 = set1.copy()
    for elem in set1:
        if elem in set2:
            new_set1.remove(elem)

    print(f"Set 1: {set1}\n"
          f"Set 2: {set2}\n"
          f"New set 1 with common elements in set 2 removed: {new_set1}")

    # Approach number 2 (more efficient)
    new_set2 = set1 - set2

    print(f"Set 1: {set1}\n"
          f"Set 2: {set2}\n"
          f"New set 1 with common elements in set 2 removed: {new_set2}")


# ex7
def exercise7(set1, set2):
    if not (isinstance(set1, set) and isinstance(set2, set)):
        raise Exception("One or both input objects are not sets!")

    if not (len(set1) > 0 and len(set2) > 0):
        raise Exception("One or both sets are empty!")

    # Case 1: Check if set1 is a subset of set2
    if set1.issubset(set2):
        difference = set2 - set1
        print(f"Set 1 is a subset of set 2.\n"
              f"The new set 2 with the elements of (sub)set 1 removed is:\n{difference}.")
    elif set2.issubset(set1):
        difference = set1 - set2
        print(f"Set 2 is a subset of set 1.\n"
              f"The new set 1 with the elements of (sub)set 2 removed is:\n{difference}.")
    elif len(set1) == len(set2):
        difference = set1 - set2
        if not difference:
            print("Set 2 is as big as set 1 and they are equal.")
        else:
            print("Set 2 is as big as set 1 but they don't have the same elements.")
    else:
        print("Neither set is a subset of the other.")


# ex8
def exercise8():



# ex9
def exercise9():



# ex10
def exercise10():



if __name__ == "__main__":
    # print("EXERCISE SET 2: Data Structures")
    # print("EX1")
    # listOne = [3, 6, 9, 12, 15, 18, 21, 8]
    # listTwo = [4, 8, 12, 16, 20, 24, 28]
    # merged_list = exercise1(listOne, listTwo)
    # print(f"The new list is:\n{merged_list}")

    # print("EX2")
    # sampleList = [34, 54, 67, 89, 11, 43, 94]
    # exercise2(sampleList)

    # print("EX3")
    # sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    # exercise3(sampleList)

    # print("EX4")
    # sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    # exercise4(sampleList)

    # print("EX5")
    # firstList = [2, 3, 4, 5, 6, 7, 8]
    # secondList = [4, 9, 16, 25, 36, 49, 64]
    # exercise5(firstList, secondList)

    # print("EX6")
    # firstSet = {23, 42, 65, 57, 78, 83, 29}
    # secondSet = {57, 83, 29, 67, 73, 43, 48}
    # exercise6(firstSet, secondSet)

    # print("EX7")
    # firstSet = {57, 83, 29}
    # secondSet = {57, 83, 29, 67, 73, 43, 48}
    # exercise7(firstSet, secondSet)

    print("EX8")
    rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
    sampleDict = {"Jhon": 47, "Emma": 69, "Kelly": 76, "Jason": 97}
    exercise8(rollNumber, sampleDict)

    print("EX9")
    speed = {'Jan': 47, 'Feb': 52, 'March': 47, 'April': 44, 'May': 52, 'June': 53, 'July': 54, 'Aug': 44, 'Sept': 54}
    exercise9(speed)

    print("EX10")
    sampleList = [87, 52, 44, 53, 54, 87, 52, 53]
    exercise10(sampleList)
