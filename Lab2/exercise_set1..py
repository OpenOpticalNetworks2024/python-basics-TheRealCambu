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


def exercise2(file_path):
    df = pd.read_csv(file_path)
    list_of_months = list(calendar.month_name)[1:]
    fig, ax = plt.subplots()
    ax.plot(df["month_number"], df["total_profit"], label="Profit data of last year", color="r",
            marker="o", markerfacecolor="k", linestyle="-", linewidth=3)
    fig.suptitle("Total Profit for each Month of the Year")
    ax.set_xticks(df["month_number"])
    ax.set_xticklabels(list_of_months, rotation=60)
    ax.yaxis.set_major_formatter('${x:.0f}')
    fig.subplots_adjust(bottom=0.2, left=0.15)
    plt.grid()
    plt.show()


def exercise3(file_path):
    df = pd.read_csv(file_path)
    months = df.iloc[:, 0]
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.suptitle("Product sales data for each month", fontsize=20)
    for column in df.columns[1:-2]:
        ax.plot(months, df[column], label=column, linewidth=2)

    plt.legend()
    plt.grid()
    plt.show()


def exercise4():
    pass


def exercise5():
    pass


def exercise6():
    pass


def exercise7():
    pass


if __name__ == "__main__":
    # print("EXERCISE SET 1")
    # print("EX1")
    # exercise1("sales_data.csv")

    # print("EX2")
    # exercise2("sales_data.csv")

    print("EX3")
    exercise3("sales_data.csv")

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
