from pathlib import Path

import pandas as pd
import numpy as np


def main():

    # Pandas data frame consists of multiple series (they represent both rows and columns)
    # Series is a one-dimensional array of indexed data
    # Series can be created from a list or array

    # Create a series from a list
    series_from_list = pd.Series([1, 2, 3, 4, 5])
    print("Series from list: ")
    print(series_from_list)
    print()

    # Create a series from a numpy array
    series_from_array = pd.Series(np.array([1, 2, 3, 4, 5]))
    print("Series from array: ")
    print(series_from_array)
    print()

    # you can also add labels to the series
    labeled_series = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
    print("Labeled series: ")
    print(labeled_series)
    print()

    # create a data frame from series
    labeled_series_2 = pd.Series([6, 7, 8, 9, 10], index=["a", "b", "c", "d", "e"])

    data_frame_from_series = pd.DataFrame(
        {"col_1": labeled_series, "col_2": labeled_series_2}
    )  # as columns
    print("Data frame from series stacked as columns: ")
    print(data_frame_from_series)
    print()

    data_frame_from_series_2 = pd.DataFrame(
        [labeled_series, labeled_series_2]
    )  # as rows
    print("Data frame from series stacked as rows: ")
    print(data_frame_from_series_2)
    print()

    # create a data frame from 2D numpy array
    data_frame_from_array = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print("Data frame from 2D array: ")
    print(data_frame_from_array)
    print()

    # create a data frame from a dictionary
    data_frame_from_dict = pd.DataFrame({"col_1": [1, 2, 3], "col_2": [4, 5, 6]})
    print("Data frame from dictionary: ")
    print(data_frame_from_dict)
    print()

    # create a data frame from csv file
    # first we need a csv file
    content = ["col_1,col_2,col_3", "1,2,3", "4,5,6", "7,8,9"]
    path = Path("data.csv")
    path.write_text("\n".join(content))
    data_frame_from_csv = pd.read_csv(path)
    path.unlink()  # delete the file
    print("Data frame from csv file: ")
    print(data_frame_from_csv)
    print()

    # we have a lot of functions implented for dealing with data frames
    # for example we can get the shape of the data frame
    print("Shape of the data frame: ")
    print(data_frame_from_csv.shape)
    print()

    # or easier, number of rows and columns
    n_rows, n_cols = data_frame_from_csv.shape
    print("Number of rows: ", n_rows)
    print("Number of columns: ", n_cols)
    print()

    # we can get the column names
    print("Column names: ")
    print(data_frame_from_csv.columns)
    print()

    # we can get the second column
    print("Second column: ")
    print(data_frame_from_csv[data_frame_from_csv.columns[1]])
    print()

    # we can get the last row
    print("Last row: ")
    print(data_frame_from_csv.iloc[-1])
    print()

    # useful statistics
    print("Mean of the data frame: ")
    print(data_frame_from_csv.mean())
    print()

    print("Mean of the second column: ")
    print(data_frame_from_csv[data_frame_from_csv.columns[1]].mean())
    print()

    # we can also transform the data frame to numpy array
    print("Data frame to numpy array: ")
    print(data_frame_from_csv.to_numpy())
    print()


if __name__ == "__main__":
    main()
