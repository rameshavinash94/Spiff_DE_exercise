import unittest
from pyunitreport import HTMLTestRunner
from UserQuerydata import QueryData
from CommisionStrategyFactory import CommissionStrategyFactory
from CalculateCommission import CalcuateCommission
from DataTransformations import JsonToDfConverter, DFJoiner
from DataValidators import DataSchemaValidators
from main import load_json

class TestCommissionStrategy(unittest.TestCase):
    
    def test_fixed_commission_strategy(self):
        """
        Test the FixedCommissionStrategy class to make sure it returns the correct commission amount for a given sales rep and date range
        """
        data = QueryData("Ian", "2023-01-01", "2023-4-30")
        commissionStrategyFactory = CommissionStrategyFactory()
        calcuateCommission = CalcuateCommission(commissionStrategyFactory)
        commission = calcuateCommission.CalculateCommission(data,"Fixed")
        self.assertEqual(commission, '55350.00')

    def test_invalid_commission_strategy(self):
        """
        Test invalid commission strategy to make sure it raises an exception.
        """
        data = QueryData("Ian", "2023-01-01", "2023-4-30")
        commissionStrategyFactory = CommissionStrategyFactory()
        calcuateCommission = CalcuateCommission(commissionStrategyFactory)
        with self.assertRaises(Exception):
            calcuateCommission.CalculateCommission(data,"Invalid")
    
    def test_json_to_df_converter(self):
        """
        Test the JsonToDfConverter class to make sure it returns the correct dataframe.
        """
        deals = load_json("https://raw.githubusercontent.com/SpiffInc/spiff_data_engineering_exercises/main/data/deals.json")
        deals_df = JsonToDfConverter(deals).convert()
        self.assertEqual(deals_df.shape, (50, 6))

    def test_df_joiner(self):
        """
        Test the DFJoiner class to make sure it returns the correct dataframe.
        """
        deals = load_json("https://raw.githubusercontent.com/SpiffInc/spiff_data_engineering_exercises/main/data/deals.json")
        products = load_json("https://raw.githubusercontent.com/SpiffInc/spiff_data_engineering_exercises/main/data/products.json")
        deals_df = JsonToDfConverter(deals).convert()
        products_df = JsonToDfConverter(products).convert()
        merged_df = DFJoiner(deals_df, products_df, 'product_id').join()
        self.assertEqual(merged_df.shape, (50, 9))
    
    def test_load_json(self):
        """
        Test the load_json function to make sure it returns the correct number of records.
        """
        deals = load_json("https://raw.githubusercontent.com/SpiffInc/spiff_data_engineering_exercises/main/data/deals.json")
        self.assertEqual(len(deals), 50)

    def test_validate_data(self, validator=DataSchemaValidators()):
        """
        Test the validate_data function to make sure it returns the correct commission amount for a given sales rep and date range
        Inject the validator class to make it easier to test.
        """

        data = QueryData("Ian", "2023-01-01", "2023-4-30")
        self.assertEqual(validator.validate_data(data), True)

    def test_empty_sales_rep_name(self, validator=DataSchemaValidators()):
        """
        Test the validate_data function to make sure it raises an exception when the sales rep name is empty.
        Inject the validator class to make it easier to test.
        """

        data = QueryData("", "2023-01-01", "2023-4-30")
        with self.assertRaises(Exception) as e:
            validator.validate_data(data)
        self.assertEqual(str(e.exception), "data cannot be empty")
    
    def test_empty_start_date(self, validator=DataSchemaValidators()):
        """
        Test the validate_data function to make sure it raises an exception when the start date is empty.
        Inject the validator class to make it easier to test.
        """

        data = QueryData("Ian", "", "2023-4-30")
        with self.assertRaises(Exception) as e:
            validator.validate_data(data)
        self.assertEqual(str(e.exception), "data cannot be empty")
    
    def test_empty_end_date(self, validator=DataSchemaValidators()):
        """
        Test the validate_data function to make sure it raises an exception when the end date is empty.
        Inject the validator class to make it easier to test.
        """

        data = QueryData("Ian", "2023-01-01", "")
        with self.assertRaises(Exception) as e:
            validator.validate_data(data)
        self.assertEqual(str(e.exception), "data cannot be empty")
    
    def test_start_date_greater_than_end_date(self, validator=DataSchemaValidators()):
        """
        Test the validate_data function to make sure it raises an exception when the start date is greater than the end date.
        Inject the validator class to make it easier to test.
        """

        data = QueryData("Ian", "2023-04-30", "2023-01-01")
        with self.assertRaises(Exception) as e:
            validator.validate_data(data)
        self.assertEqual(str(e.exception), "start_date must be before end_date")

    def test_start_date_format(self, validator=DataSchemaValidators()):
        """
        Test the validate_data function to make sure it raises an exception when the start date is not in the correct format.
        Inject the validator class to make it easier to test.
        """

        data = QueryData("Ian", "01-2022-01", "2023-4-30")
        with self.assertRaises(Exception) as e:
            validator.validate_data(data)
        self.assertEqual(str(e.exception), "start_date must be in the format YYYY-MM-DD")

    def test_end_date_format(self, validator=DataSchemaValidators()):
        """
        Test the validate_data function to make sure it raises an exception when the end date is not in the correct format.
        Inject the validator class to make it easier to test.
        """

        data = QueryData("Ian", "2023-01-01", "4-2021-3")
        with self.assertRaises(Exception) as e:
            validator.validate_data(data)
        self.assertEqual(str(e.exception), "end_date must be in the format YYYY-MM-DD")

    def test_sales_rep_name_not_exist(self, validator=DataSchemaValidators()):
        """
        Test the validate_data function to make sure it raises an exception when the sales rep name does not exist in the sales_data.csv file.
        Inject the validator class to make it easier to test.
        """
        data = QueryData("Ian1", "2023-01-01", "2023-4-30")
        with self.assertRaises(Exception) as e:
            validator.validate_data(data)
        self.assertEqual(str(e.exception), "sales_rep_name must be in the sales_data.csv file")

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='test-reports'))