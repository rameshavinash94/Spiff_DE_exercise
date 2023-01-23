from abc import ABCMeta, abstractmethod
import pandas as pd

class SalesDataInterface(metaclass=ABCMeta):
    """
    SalesDataInterface is an interface that defines the methods that a class must implement.
    """
    @abstractmethod
    def get_sales_data(self):
        pass

class SalesDataSingleton(SalesDataInterface):
    """
    SalesDataSingleton is a singleton class that holds the sales data.
    """
    __instance = None

    @staticmethod
    def get_instance():
        """
        Static access method. This method returns the singleton instance.

        Returns:
            SalesDataSingleton : SalesDataSingleton instance
        """
        if SalesDataSingleton.__instance is None:
            SalesDataSingleton()
        return SalesDataSingleton.__instance
    
    def __init__(self, sales_data : pd.DataFrame):
        """
        Private constructor. This method initializes the singleton instance.

        Args:
            sales_data (pd.DataFrame): Pandas DataFrame

        Raises:
            Exception: This class is a singleton!
        """
        if SalesDataSingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.sales_data = sales_data
            SalesDataSingleton.__instance = self

    def get_sales_data(self) -> pd.DataFrame:
        """
        Get the sales data.

        Returns:
            pd.DataFrame: The sales data
        """
        return self.sales_data