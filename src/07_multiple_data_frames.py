import numpy as np
import pandas as pd


def main():

    data_frame_a = pd.DataFrame(
        np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["A", "B", "C"]
    )
    data_frame_b = pd.DataFrame(
        np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]]), columns=["D", "E", "F"]
    )

    ## one below the other
    print("One below the other")
    print(pd.concat([data_frame_a, data_frame_b], axis=0))
    print()

    # they need to have the same columns
    print(
        pd.concat(
            [data_frame_a, data_frame_b.rename(columns={"D": "A", "E": "B", "F": "C"})],
            axis=0,
        )
    )
    print()

    ## side by side
    print("Side by side")
    print(pd.concat([data_frame_a, data_frame_b], axis=1))
    print()

    # merge data frames with different column names
    print("Merge data frames")
    print(pd.merge(data_frame_a, data_frame_b, left_index=True, right_index=True))
    print()

    # merge data frames when one column has the same name
    print("Merge data frames with same column name")
    another_data_frame = pd.DataFrame(
        np.array([[1, 2, 3], [13, 14, 15], [16, 17, 18]]), columns=["A", "X", "XX"]
    )
    print(pd.merge(data_frame_a, another_data_frame, on="A"))
    print()

    # outer join
    print("Outer join")
    print(pd.merge(data_frame_a, another_data_frame, on="A", how="outer"))
    print()

    # inner join
    print("Inner join")
    print(pd.merge(data_frame_a, another_data_frame, on="A", how="inner"))
    print()

    # left join
    print("Left join")
    print(pd.merge(data_frame_a, another_data_frame, on="A", how="left"))
    print()

    # right join
    print("Right join")
    print(pd.merge(data_frame_a, another_data_frame, on="A", how="right"))
    print()


if __name__ == "__main__":
    main()
