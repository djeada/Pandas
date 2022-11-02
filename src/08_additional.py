from typing import List
import pandas as pd

extracted_tables: List[pd.DataFrame] = pd.read_html(
    "https://en.wikipedia.org/wiki/Poverty"
)
print(extracted_tables)
