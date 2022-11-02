import numpy as np
import pandas as pd


def main():

    data_frame = pd.DataFrame(
        np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["A", "B", "C"]
    )

    # select row by index
    print("Select row on index 1")
    print(data_frame.iloc[1])
    print()

    # select multiple rows by index
    print("Select rows on indices from 0 to 1")
    print(data_frame.iloc[0:2])

    # exchange row with a list
    example_list = [10, 20, 30]
    data_frame.iloc[0] = example_list
    print("Exchange row 0 with a list")
    print(data_frame)

    # append row at the end of the data frame
    data_frame.loc[3] = [100, 200, 300]
    print("Append row 3 at the end of the data frame")
    print(data_frame)

    # add row with values 1, 2, 3 at index 1
    data_frame.loc[1] = [1, 2, 3]
    print("Add row 1 at index 1")
    print(data_frame)

    # drop row at index 1
    data_frame.drop(data_frame.index[1], axis=0, inplace=True)
    print("Drop row at index 1")
    print(data_frame)


if __name__ == "__main__":
    main()
