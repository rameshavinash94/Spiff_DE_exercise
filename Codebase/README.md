# Spiff Data Engineering Candidate Coding Exercises
  
For this exercise, I wrote a python script that calculates the commission for a sales rep.

The main requirement is to pass the following arguments to a function:
> 
> - sales_rep_name (str): Sales rep name.
> 
> - start_date (str): Start date.
> 
> - end_date (str): End date.

 The function  should calculate the commission for the sales rep between the start and end dates.

***This can be done in a simple  functional programming approach with few lines fo code but i have followed the object oriented programming principles and  exceptional handling techniques to achieve this such that the code is more readable, maintainable, testable and can be extended to include more features in the future.***  

 - Have followed the SOLID principles of OOP and have used the Factory pattern and the Strategy pattern to achieve.
 
 - The Factory pattern is used to create the JsonLoaderFactory class which is used to create the JsonLoader class.

 - The JsonLoader class is used to load the json data from the deals.json and products.json files.

 - The Factory pattern is used to create the CommissionStrategyFactory class which is used to create the CommissionStrategy class.

 - The Strategy pattern is used to create the CommissionStrategy class which is used to calculate the commission for the sales rep. So, in the future if we want to change the commission calculation criteria, we can create a new class that inherits from the CommissionStrategy class and implement the calculate_commission method to calculate the commission based on the new criteria.

 - The CommissionStrategy class is used to calculate the commission for the sales rep.

 - The DataValidators class is used to validate the data.

 - The JsonToDfConverter class under the DataTransformations module is used to convert the json data to a pandas dataframe.

 - The DFMerger class under the DataTransformations module is used to merge the deals_df and products_df dataframes on the product_id and id column accordingly.

 - The CalcuateCommission class is used to calculate the commission for the sales rep.

 - The QueryData class is used to input the data into a dataclass.

 - The SalesDataSingleton class is a singleton class that holds the sales data.the reason for this class is to avoid reading the sales data from the csv file every time the data is validated.the sales data is read from the csv file only once and then stored in the singleton class.

 - The main.py file is used to run the script.
 
 - The test_commissioncalculation_criterias.py file is used to perform unit testing on the script

## STEPS TO RUN THE PROJECT

1. Install python 3.8 or above

2. Create a Project Directory and redirect to the directory using the below Commands 

```
mkdir DEexercise
cd DEexercise
```

3. Next, run the script below within the directory to create the virtual environment 

```
python3 -m venv env
```

4. activate the virtual environment by running the  below command 

```
source env/bin/activate
```

5. Clone the below Github Repo to the project directory using SSH/Https and git Credentials
Repo: https://github.com/rameshavinash94/Spiff_DE_exercise

6. Once done, Redirect to Codebase directory 

```
cd DEexercise/Spiff_DE_exercise/Codebase
```

7. Install all the project requirements using below command

```
 pip install -r requirements.txt
 
```

8. To run the code . Use the below command

```
python main.py
```

9. To generate test report, run the below command

```
python test_commissioncalculation_criterias.py
```

## SAMPLE SNIPPET AFTER RUNNING
<img width="671" alt="Screen Shot 2023-01-21 at 8 34 28 PM" src="https://user-images.githubusercontent.com/87649563/213900797-b8e4a8e6-9dd2-4543-8265-17cbf6608519.png">

## SAMPLE TEST REPORT SNIPPET
<img width="1072" alt="Screen Shot 2023-01-21 at 8 36 29 PM" src="https://user-images.githubusercontent.com/87649563/213900849-29289e18-8ba4-40d3-8643-279a6ab1aea3.png">
