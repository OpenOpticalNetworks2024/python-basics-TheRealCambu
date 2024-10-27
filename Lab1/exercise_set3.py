"""Exercise Set 3: Numpy Exercises"""

import numpy as np
import matplotlib as plt


# ex1
def exercise1():
    random_integers = np.random.randint(0, 10, size=(4, 2), dtype=np.uint8)
    print("Array:\n", random_integers)

    print("Attributes:")
    print("Shape:", random_integers.shape)
    print("Size:", random_integers.size)
    print("Data type:", random_integers.dtype)
    print("Number of dimensions:", random_integers.ndim)
    print("Memory size (bytes):", random_integers.nbytes)


# ex2
def exercise2():
    random_vect = np.arange(100, 200, 10).reshape((5, 2))
    print(random_vect)


# ex3
def exercise3(list_of_lists):
    return list_of_lists[:, 2]


# ex4
def exercise4(list_of_lists):
    return list_of_lists[1::2, 0::2]


# ex5
def exercise5(list_of_lists1, list_of_lists2):
    return np.sqrt(list_of_lists1 + list_of_lists2)


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
    # print("EXERCISE SET 3: NumPy Exercises")
    # print("EX1")
    # exercise1()

    # print("EX2")
    # exercise2()

    # print("EX3")
    # l_o_l = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
    # output = exercise3(l_o_l)
    # print(output)

    # print("EX4")
    # l_o_l = np.array([[3, 6, 9, 12], [15, 18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])
    # output = exercise4(l_o_l)
    # print(output)

    # print("EX5")
    # l_o_l_1 = np.array([[5, 6, 9], [21, 18, 27]])
    # l_o_l_2 = np.array([[15, 33, 24], [4, 7, 1]])
    # output = exercise5(l_o_l_1, l_o_l_2)
    # print("Array 1:\n", l_o_l_1)
    # print("Array 2:\n", l_o_l_2)
    # print("Sum of np arrays and then apply sqrt:\n", output)

    print("EX6")
    exercise6()

    print("EX7")
    exercise7()

    print("EX8")
    exercise8()
