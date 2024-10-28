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


def exercise5(df):
    # Create a list of month names for labeling the x-axis
    months_list = list(calendar.month_name)[1:]

    # Create a figure and axis for the bar plot
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plotting the bar chart
    ax.bar(df["month_number"], df["bathingsoap"], color='skyblue', edgecolor='black')

    # Setting the title and labels
    fig.suptitle("Bar chart of the bathing soap sells", fontsize=20, fontweight='bold')
    ax.set_ylabel("Item sold", fontsize=16)

    # Customizing x-ticks
    ax.set_xticks(df["month_number"])
    ax.set_xticklabels(months_list, rotation=60, ha="right", fontsize=12)

    # Adjust layout to make room for x-labelsù
    fig.subplots_adjust(bottom=0.2)

    # Display the plot
    plt.grid(axis="y", linestyle="--", alpha=0.7)  # Adding a grid for better readability
    plt.tight_layout()  # Automatically adjust subplot parameters for a better fit
    plt.show()


def exercise6(df):
    plt.plot(figsize=(12, 8))
    plt.hist(df["total_profit"], color="skyblue", edgecolor="black", alpha=0.7)
    plt.title("Histogram of the total profit for each month", fontsize=15, fontweight="bold")
    plt.xlabel("Total Profit", fontsize=13)
    plt.ylabel("Frequency", fontsize=13)
    plt.grid(axis="y", linestyle="--", alpha=0.8)
    plt.tight_layout()
    plt.show()


def exercise7(df):
    month_list = list(calendar.month_name)[1:]
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.suptitle("Facewash sell every month", fontsize=20, fontweight="bold")
    ax.plot(df["month_number"], df["facewash"])
    ax.set_ylabel("Sells", fontsize=16)
    ax.set_xticks(df["month_number"])
    ax.set_xticklabels(month_list, rotation=60, ha="right", fontsize=12)
    plt.grid(linestyle="-.", alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    dataframe_df = pd.read_csv("sales_data.csv")

    print("EXERCISE SET 1")
    print("EX1")
    exercise1(dataframe_df)

    print("EX2")
    exercise2(dataframe_df)

    print("EX3")
    exercise3(dataframe_df)

    print("EX4")
    exercise4(dataframe_df)

    print("EX5")
    exercise5(dataframe_df)

    print("EX6")
    exercise6(dataframe_df)

    print("EX7")
    exercise7(dataframe_df)
