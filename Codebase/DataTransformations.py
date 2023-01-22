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

class DFJoiner:
    """
    Join two Pandas DataFrames.
    """
    def __init__(self, df1, df2, on):
        self.df1 = df1
        self.df2 = df2
        self.on = on

    def join(self) -> pd.DataFrame:
        """
        Join two Pandas DataFrames.

        Returns:
            pd.DataFrame : Pandas DataFrame
        """
        joined_df = self.df1.join(self.df2.set_index('id'), on=self.on)
        return joined_df