import numpy as np
import pandas as pd


def main():

    data_frame = pd.DataFrame(
        np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["A", "B", "C"]
    )

    # select rows where column 'A' is divisible by 2
    print("Select rows where column A is divisible by 2")
    print(data_frame[data_frame["A"] % 2 == 0])
    print()

    # show which values are divisible by 3
    print("Show which values are divisible by 3")
    print(data_frame % 3 == 0)
    print()

    # show 'group by' result
    print("Show group by result")
    print(data_frame.groupby("A").sum())
    print()

    # well not much has changed, that's because we don't have repetitions in our datafram
    # let's use different example
    data_frame = pd.DataFrame(
        [
            ["A", "Adam", 435],
            ["B", "Morgan", 42],
            ["C", "Khaled", 234],
            ["A", "Xi", 524],
            ["C", "James", 455],
            ["C", "Nicko", 1000],
        ],
        columns=["Favorite Drink", "Name", "Units Consumed"],
    )

    print(data_frame.groupby("Favorite Drink").mean(numeric_only=True))
    print(data_frame.groupby("Favorite Drink").sum(numeric_only=True))
    print(data_frame.groupby("Favorite Drink").agg([np.mean, min, max]))

    # sort by column 'Units Consumed'
    print("Sort by column Units Consumed")
    print(data_frame.sort_values(by="Units Consumed"))
    print()

    # filter rows where column 'Units Consumed' is greater than 400
    print("Filter rows where column Units Consumed is greater than 400")
    print(data_frame[data_frame["Units Consumed"] <= 400])
    print()

    # show only numeric columns
    print("Show only numeric columns")
    print(data_frame.select_dtypes(include=[np.number]))
    print()

    # show only non-numeric columns
    print("Show only non-numeric columns")
    print(data_frame.select_dtypes(exclude=[np.number]))
    print()


if __name__ == "__main__":
    main()
