from CommissionStrategyInterface import CommissionStrategy
from UserQuerydata  import QueryData
import pandas as pd
from SalesDataSingleton import SalesDataSingleton

class FixedCommissionStrategy(CommissionStrategy):
    """
    FixedCommissionStrategy is a class that calculates the commission for a fixed commission type
    """

    def CalculateCommission(self,data:QueryData) -> float:
        """
        CalculateCommission is a method that calculates the commission for a fixed commission type
        Formula: (quantity_products_sold * product_amount * commission_rate)
        
        Args:
            data (QueryData): QueryData is a dataclass that contains the data needed to calculate the commission

        Returns:
            float: The total commission
        """        
        #Get the sales rep name from the data
        sales_rep_name = data.sales_rep_name

        #Get the start date from the data
        start_date = pd.to_datetime(data.start_date)

        #Get the end date from the data
        end_date = pd.to_datetime(data.end_date)

        # #read the sales data from the csv file
        # sales_data = pd.read_csv("sales_data.csv")

        # read the sales data from the Singleton class
        sales_data = SalesDataSingleton.get_instance().get_sales_data()

        #change the date column to a datetime object
        sales_data['date'] = pd.to_datetime(sales_data['date'])

        #filter the filtered_df to only include deals that were closed by the sales_rep_name
        filtered_df = sales_data[sales_data['sales_rep_name'] == sales_rep_name]
        
        #filter the merged_df to only include deals that were closed between the start and end date
        final_df = filtered_df[(filtered_df['date'] >= start_date) & (filtered_df['date'] <= end_date)]
    
        #calculate the total commission for the sales_rep_name
        commission = final_df['quantity_products_sold'] * final_df['product_amount'] * final_df['commission_rate']
        total_commission = commission.sum()
        
        return '{:.2f}'.format(total_commission)
