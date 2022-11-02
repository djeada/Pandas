import numpy as np
import pandas as pd


def main():

    data_frame = pd.DataFrame(
        np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["A", "B", "C"]
    )

    # select column 'A'
    print("Select column A")
    print(data_frame["A"])
    print()

    # select column by index
    print("Select column on index 1")
    print(data_frame.iloc[:, 1])
    print()

    # select multiple columns by index
    print("Select columns on indices from 0 to 1")
    print(data_frame.iloc[:, 0:2])
    print()

    # exchange column with a list
    example_list = [10, 20, 30]
    data_frame["C"] = example_list
    print("Exchange column C with a list")
    print(data_frame)
    print()

    # append column at the end of the data frame
    data_frame["D"] = ["dog", "cat", "bird"]
    print("Append column D at the end of the data frame")
    print(data_frame)
    print()

    # add column 'E' with values 1, 2, 3 at index 1
    data_frame.insert(1, "E", [1, 2, 3])
    print("Add column E at index 1")
    print(data_frame)
    print()

    # drop column 'E'
    data_frame.drop("E", axis=1, inplace=True)
    print("Drop column E")
    print(data_frame)
    print()

    # drop column at index 1
    data_frame.drop(data_frame.columns[1], axis=1, inplace=True)
    print("Drop column at index 1")
    print(data_frame)
    print()

    # remove non-numeric columns
    def remove_non_numeric_columns(data_frame):
        non_floats = []
        for col in data_frame:
            if not pd.api.types.is_numeric_dtype(data_frame[col]):
                non_floats.append(col)
        result = data_frame.drop(columns=non_floats)
        return result

    print("Remove non-numeric columns")
    result = remove_non_numeric_columns(data_frame)
    print(result)

    # rename columns 'A' to 'geography' and 'D' to 'age' and 'C' to 'income'
    data_frame.rename(
        columns={"A": "geography", "D": "age", "C": "income"}, inplace=True
    )
    print("Rename columns")
    print(data_frame)
    print()


if __name__ == "__main__":
    main()
