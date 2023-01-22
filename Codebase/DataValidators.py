import pandas as pd
#import datetime

class DataSchemaValidators:
    def validate_data(self,data) -> bool:
        """
        Validate the data

        Args:
            data (QueryData): QueryData is a dataclass that contains the data needed to calculate the commission

        Raises:
            ValueError: data cannot be null
            ValueError: data cannot be empty
            TypeError: sales_rep_name must be a string
            TypeError: start_date must be a string
            TypeError: end_date must be a string
            ValueError: start_date must be in the format YYYY-MM-DD
            ValueError: end_date must be in the format YYYY-MM-DD
            ValueError: start_date must be before end_date
            ValueError: sales_rep_name must be in the sales_data.csv file

        Returns:
            bool: True if the data is valid
        """

        #validate the data is not null
        if data is None:
            raise ValueError("data cannot be null")
        
        #validate the data is not empty
        if data.sales_rep_name == "" or data.start_date == "" or data.end_date == "":
            raise ValueError("data cannot be empty")

        #validate the datatypes
        if not isinstance(data.sales_rep_name, str):
            raise TypeError("sales_rep_name must be a string")
        if not isinstance(data.start_date, str):
            raise TypeError("start_date must be a string")
        if not isinstance(data.end_date, str):
            raise TypeError("end_date must be a string")

        #validate the date format
        try:
            pd.to_datetime(data.start_date)
        except ValueError:
            raise ValueError("start_date must be in the format YYYY-MM-DD")
        try:
            pd.to_datetime(data.end_date)
        except ValueError:
            raise ValueError("end_date must be in the format YYYY-MM-DD")
        
        #validate the start date is before the end date
        if pd.to_datetime(data.start_date) > pd.to_datetime(data.end_date):
            raise ValueError("start_date must be before end_date")

        ''' 
        #validate start_date and end_date are greater than current date
        # the below validations is not needed and does not work since the data is mocked and the dates are made up
        # if pd.to_datetime(data.start_date) > pd.to_datetime(datetime.now().strftime("%Y-%m-%d")):
        #     raise ValueError("start_date must be before current date")
        
        # if pd.to_datetime(data.end_date) > pd.to_datetime(datetime.now().strftime("%Y-%m-%d")):
        #     raise ValueError("end_date must be before current date")
            
        '''

        #validate the sales rep name is in the sales_data.csv file
        sales_data = pd.read_csv("sales_data.csv")
        sales_rep_names = sales_data['sales_rep_name'].unique()
        if data.sales_rep_name not in sales_rep_names:
            raise ValueError("sales_rep_name must be in the sales_data.csv file")

        return True