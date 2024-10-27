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
    # print("EXERCISE SET 3: NumPy Exercises")
    # print("EX1")
    # exercise1()

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
