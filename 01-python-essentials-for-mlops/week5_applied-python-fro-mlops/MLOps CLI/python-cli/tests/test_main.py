import pandas as pd
from csv_linter.main import unnamed_columns


def test_no_unnamed_columns():
    df = pd.DataFrame()
    assert unnamed_columns(df) == 0
