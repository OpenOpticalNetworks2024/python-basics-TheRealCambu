"""Exercise Set 1: Python Basics"""

import numpy as np
import matplotlib as plt


# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    print("Insert two integer numbers:\n")
    num1 = int(input())
    num2 = int(input())
    prod = num1 * num2
    if prod > 1000:
        return num1 + num2
    else:
        return prod


# ex2
def exercise2(start_num):
    # Check if the input is a valid integer and non-negative
    if not isinstance(start_num, int) or start_num < 0:
        raise Exception("The inserted number is not a valid non-negative integer!\n")

    max_num = 10

    # Check if the input exceeds the maximum limit
    if start_num > (max_num - 1):
        raise Exception("The inserted i-th number: " + str(start_num) +
                        " is greater than the maximum allowed value in the range = " +
                        str(max_num - 1) + "\n")

    # Create a range from 0 to max_num (exclusive)
    x = range(max_num)

    # Iterate through the range and print the results
    for i, _ in enumerate(x):
        if i >= start_num:
            if i == 0:
                print(f"{x[i]}")
            else:
                print(f"{x[i]} + {x[i - 1]} = {x[i] + x[i - 1]}")


# ex3
def exercise3(input_list):
    if not isinstance(input_list, list):
        raise Exception("The input is not a list!\n")

    for elem in input_list:
        if not isinstance(elem, int):
            raise Exception("Some elements in the list are not integers!\n")

    if len(input_list) == 0:
        raise Exception("The input is an empty list!\n")

    if len(input_list) == 1:
        print("The first and the last numbers are the same because the list only has one element!\n")

    if input_list[0] == input_list[-1]:
        print("The first and the last elements of the list are equal!")
    else:
        print("The first and the last elements of the list are not equal!")


# ex4
def exercise4(input_list):
    if not isinstance(input_list, list):
        raise Exception("The input is not a list!\n")

    for elem in input_list:
        if not isinstance(elem, int):
            raise Exception("Some elements in the list are not integers!\n")

    if len(input_list) == 0:
        raise Exception("The input is an empty list!\n")

    for elem in input_list:
        if elem % 5 == 0:
            print(str(elem) + " is divisible by 5!")
        else:
            print(str(elem) + " is not divisible by 5!")


# ex5
def exercise5():
    fixed_str = "Emma is a good developer. Emma is also a writer"
    str_to_search = "Emma"
    counter = 0
    for elem in fixed_str.split(' '):
        if str_to_search in elem:
            counter += 1
    print(f"The string {str_to_search} appeared {counter} times in the string \"{fixed_str}\"")


# ex6
def exercise6(input_list):
    if not isinstance(input_list, list):
        raise Exception("The input is not a list!\n")

    for elem in input_list:
        if not isinstance(elem, int):
            raise Exception("Some elements in the list are not integers!\n")

    if len(input_list) == 0:
        raise Exception("The input is an empty list!\n")

    new_list_odd_numbers = []

    for elem in input_list:
        if elem % 2 != 0:
            new_list_odd_numbers.append(elem)

    if new_list_odd_numbers:
        print(f"The original list is: {input_list}\n"
              f"The new list is: {new_list_odd_numbers}")
    else:
        print("The new list is empty!")


# ex7
def exercise7(str1, str2):
    if not (isinstance(str1, str) or isinstance(str2, str)):
        raise Exception("One or both inputs are not strings!")

    len_str1 = len(str1)
    if not (len_str1 > 0 and len(str2) > 0):
        raise Exception("One or both strings are empty!")

    if len_str1 == 1:
        merged_str = str2 + str1
    else:
        first_part, second_part = str1[:len_str1 // 2], str1[len_str1 // 2:]
        merged_str = first_part + str2 + second_part

    print(f"The final merged string is: {merged_str}")

    return merged_str


# ex8
def exercise8(str1, str2):
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise Exception("One or both inputs are not strings!")

    len_str_1 = len(str1)
    len_str_2 = len(str2)
    if not (len_str_1 > 2 and len_str_2 > 2):
        raise Exception("One or both strings are too short to be processed!")

    middle_char_idx_str1 = len_str_1 // 2
    middle_char_idx_str2 = len_str_2 // 2
    final_str = str1[0] + str1[middle_char_idx_str1] + str1[-1] + str2[0] + str2[middle_char_idx_str2] + str2[-1]
    print(f"The final merged string is: {final_str}")
    return final_str


# ex9
def exercise9(str1):
    if not (isinstance(str1, str) or isinstance(str2, str)):
        raise Exception("One or both inputs are not strings!")

    len_str1 = len(str1)
    if not (len_str1 > 0 and len(str2) > 0):
        raise Exception("One or both strings are empty!")


# ex10
def exercise10():
    pass


# ex11
def exercise11():
    pass


# ex12
def exercise12():
    pass


if __name__ == "__main__":
    # print("EXERCISE SET 1")
    # print("EX1")
    # exercise1()

    # print("EX2")
    # exercise2(3)

    # print("EX3")
    # exercise3([1, 2, 3, 1])

    # print("EX4")
    # exercise4([5, 10, 2, 25])

    # print("EX5")
    # exercise5()

    # print("EX6")
    # exercise6([5, 10, 2, 25])

    # print("EX7")
    # final_string = exercise7("Mimmo special", "Merge")

    # print("EX8")
    # final_string = exercise8("hello", "world")

    print("EX9")
    exercise9()

    print("EX10")
    exercise10()

    print("EX11")
    exercise11()

    print("EX12")
    exercise12()
