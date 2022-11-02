import numpy as np
import pandas as pd


def main():

    data_frame = pd.DataFrame(
        np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["A", "B", "C"]
    )

    # all rows except row 1
    print("All rows except row 1")
    print(data_frame.drop(data_frame.index[1], axis=0))
    print()

    # rows between index 0 and 1
    print("Rows between index 0 and 1")
    print(data_frame.iloc[0:2])
    print()

    # all columns except column 'A'
    print("All columns except column A")
    print(data_frame.drop("A", axis=1))
    print()

    # columns between index 0 and 1
    print("Columns between index 0 and 1")
    print(data_frame.iloc[:, 0:2])
    print()


if __name__ == "__main__":
    main()
