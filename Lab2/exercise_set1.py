import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import calendar


def exercise1(df):
    list_of_months = list(calendar.month_name)[1:]
    plt.plot(df["month_number"], df["total_profit"])
    plt.ylabel("Total Profit")
    plt.xticks(df["month_number"], labels=list_of_months, rotation=60)
    plt.subplots_adjust(bottom=0.2, left=0.15)
    plt.grid()
    plt.show()


def exercise2(df):
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


def exercise3(df):
    months = list(calendar.month_name)[1:]
    months_numbers = df.iloc[:, 0]
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.suptitle("Product sales data for each month", fontsize=20)
    fig.subplots_adjust(bottom=0.15)
    for column in df.columns[1:-2]:
        ax.plot(months_numbers, df[column], label=column, linewidth=2)

    ax.set_ylabel("Product sold", fontsize=14)
    ax.set_xticks(months_numbers)
    ax.set_xticklabels(months, rotation=60, fontsize=13)
    plt.legend()
    plt.grid()
    plt.show()


def exercise4(df):
    months_list = list(calendar.month_name)[1:]  # Get month names for x-axis labels

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.suptitle("Toothpaste Sales Over the Year", fontsize=18)

    # Scatter plot with improved marker size and color
    ax.scatter(df["month_number"], df["toothpaste"], s=150, marker="p", color="blue", edgecolor="red")
    ax.set_xlabel("Months", fontsize=16)
    ax.set_ylabel("Sales (in units)", fontsize=16)

    # Set month names as x-ticks
    ax.set_xticks(df["month_number"])
    ax.set_xticklabels(months_list, rotation=45, ha="right", fontsize=12)

    # Adjust layout and add grid
    fig.subplots_adjust(bottom=0.2)
    ax.grid(visible=True, linestyle='--', alpha=0.7)

    plt.show()


def exercise5():
    pass


def exercise6():
    pass


def exercise7():
    pass


if __name__ == "__main__":
    dataframe_df = pd.read_csv("sales_data.csv")

    # print("EXERCISE SET 1")
    # print("EX1")
    # exercise1(dataframe_df)
    #
    # print("EX2")
    # exercise2(dataframe_df)
    #
    # print("EX3")
    # exercise3(dataframe_df)

    print("EX4")
    exercise4(dataframe_df)

    # print("EX5")
    # exercise5()
    #
    # print("EX6")
    # exercise6()
    #
    # print("EX7")
    # exercise7()
