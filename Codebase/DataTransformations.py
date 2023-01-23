import pandas as pd

class JsonToDfConverter:
    """
    Convert JSON data to a Pandas DataFrame.
    """
    def __init__(self, json):
        self.json = json

    def convert(self) -> pd.DataFrame:
        """
        Convert JSON data to a Pandas DataFrame.

        Returns:
            pd.DataFrame : Pandas DataFrame
        """
        
        df = pd.json_normalize(self.json)
        return df

class DFMerger:
    """
    Merge two Pandas DataFrames.
    """
    def __init__(self, df1, df2, lefton, righton):
        self.df1 = df1
        self.df2 = df2
        self.lefton = lefton
        self.righton = righton

    def merge(self) -> pd.DataFrame:
        """
        Join two Pandas DataFrames.

        Returns:
            pd.DataFrame : Pandas DataFrame
        """
        joined_df = pd.merge(self.df1, self.df2, left_on=self.lefton, right_on=self.righton)
        return joined_df