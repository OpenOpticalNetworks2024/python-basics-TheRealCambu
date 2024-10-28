import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import calendar


def exercise1(file_path):
    df = pd.read_csv(file_path)
    list_of_months = list(calendar.month_name)[1:]
    plt.plot(df["month_number"], df["total_profit"])
    plt.ylabel("Total Profit")
    plt.xticks(df["month_number"], labels=list_of_months, rotation=60)
    plt.subplots_adjust(bottom=0.2, left=0.15)
    plt.grid()
    plt.show()


def exercise2():
    pass


def exercise3():
    pass


def exercise4():
    pass


def exercise5():
    pass


def exercise6():
    pass


def exercise7():
    pass


if __name__ == "__main__":
    print("EXERCISE SET 1")
    print("EX1")
    exercise1("sales_data.csv")

    # print("EX2")
    # exercise2()
    #
    # print("EX3")
    # exercise3()
    #
    # print("EX4")
    # exercise4()
    #
    # print("EX5")
    # exercise5()
    #
    # print("EX6")
    # exercise6()
    #
    # print("EX7")
    # exercise7()
