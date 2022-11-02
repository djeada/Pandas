import numpy as np
import pandas as pd


def main():
    data_frame = pd.DataFrame(
        np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["A", "B", "C"]
    )

    # get a cell by row and column index
    print(f"Cell at row 1, column 2: {data_frame.iloc[1, 2]}")
    print()

    # get a cell by row and column name
    print(f'Cell at row 1, column B: {data_frame.loc[1, "B"]}')
    print()

    # change a cell by row and column index
    value = 100
    data_frame.iloc[1, 2] = value
    print(f"Change cell at row 1, column 2 to: {value}")
    print(data_frame)
    print()

    # apply lambda x : x**2 to the first column
    data_frame["A"] = data_frame["A"].apply(lambda x: x ** 2)
    print("Apply lambda x : x**2 to the first column")
    print(data_frame)
    print()

    # add column 'sex' with values 'male' and 'female'
    data_frame["sex"] = ["male", "female", "female"]
    print(data_frame)
    print()

    # change male to 0 and female to 1
    data_frame["sex"] = [0 if x == "male" else 1 for x in data_frame["sex"]]
    print("Encoding male as 0 and female as 1")
    print(data_frame)
    print()

    # show how many null values in the data frame

    null_values = data_frame.isnull().sum()
    print("Number of null values in each column")
    print(null_values)
    print()

    # let's put null values at 5 random cells
    for x, y in zip(np.random.randint(0, 3, 5), np.random.randint(0, 3, 5)):
        data_frame.iloc[x, y] = np.nan

    print("Data frame with null values")
    print(data_frame)
    print()

    # show how many null values in the data frame
    null_values = data_frame.isnull().sum()
    print("Number of null values in each column")
    print(null_values)
    print()

    def any_null_value(data_frame):
        return data_frame.isnull().values.any()

    # copy the data frame and drop rows with null values
    data_frame_without_nulls = data_frame.copy()
    data_frame_without_nulls.dropna(inplace=True)
    print("Data frame without null values")
    print(data_frame_without_nulls)
    print()

    # fill the null values with mean of the column in the original data frame
    data_frame.fillna(data_frame.mean(), inplace=True)
    print("Data frame with null values filled with mean")
    print(data_frame)
    print()


if __name__ == "__main__":
    main()
