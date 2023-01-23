from JsonLoadersFactory import JsonLoaderFactory
from CommisionStrategyFactory import CommissionStrategyFactory
from UserQuerydata import QueryData
from DataValidators import DataSchemaValidators
from CalculateCommission import CalcuateCommission
from DataTransformations import JsonToDfConverter, DFMerger
from SalesDataSingleton import SalesDataSingleton

def load_json(source) -> dict:
    """
    Load JSON data from a file or URL.

    Args:
        source (str): Path to a file or URL.

    Returns:
        dict : JSON data.
    """
    factory = JsonLoaderFactory()
    loader = factory.get_loader(source)
    return loader.load()

def calculate_commission(sales_rep_name, start_date, end_date,commissionType="Fixed") -> float:
    """
    Calculate commission for a sales rep.

    Args:
        sales_rep_name (str): Sales rep name.
        start_date (str): Start date.
        end_date (str): End date.

    Returns:
        float: Commission.
    """

    #input the data into a QueryData dataclass
    data = QueryData(sales_rep_name, start_date, end_date)

    #validate the data
    dataValidators = DataSchemaValidators()
    dataValidators.validate_data(data)
   
    #calculate the commission
    commissionStrategyFactory = CommissionStrategyFactory()
    calcuateCommission = CalcuateCommission(commissionStrategyFactory)
    commission = calcuateCommission.CalculateCommission(data,commissionType)
    return commission

def PrintCommission(sales_rep_name, start_date, end_date):
    """
    Print the commission for a sales rep.

    Args:
        sales_rep_name (str): Sales rep name.
        start_date (str): Start date.
        end_date (str): End date.
    """
    commission = calculate_commission(sales_rep_name, start_date, end_date)
    print(f"Commission for {sales_rep_name} between {start_date} and {end_date} is {commission}")

if __name__ == "__main__":
    #deals.json url
    deals = load_json("/Users/avinash/Desktop/DEexercise/Spiff_DE_exercise-main/data/deals.json")
    #products.json url
    products = load_json("/Users/avinash/Desktop/DEexercise/Spiff_DE_exercise-main/data/products.json")

    #convert the deals.json file to a pandas dataframe
    deals_df = JsonToDfConverter(deals).convert()

    #convert the products.json file to a pandas dataframe
    products_df = JsonToDfConverter(products).convert()

    # Merge the deals_df and products_df dataframes on the product_id column from deals and the id column from products
    merged_df = DFMerger(deals_df, products_df, 'product_id','id').merge()

    #write the merged results to csv
    merged_df.to_csv('sales_data.csv', index=False)

    #save the merged results to a singleton class
    sales_data = SalesDataSingleton(merged_df)
    
    #calculate and print the total commission for sales_rep_name 'Ian' between 2023-01-01 and 2023-4-30
    PrintCommission('Ian','2023-01-01', '2023-4-30')

    #calculate  and print the total commission for sales_rep_name 'David' between 2023-04-01 and 2023-06-30
    PrintCommission('David','2023-04-01', '2023-06-30')

    #calculate and print the total commission for sales_rep_name 'Poppy' between 2023-03-01 and 2023-5-30
    PrintCommission('Poppy','2023-03-01', '2023-5-30')