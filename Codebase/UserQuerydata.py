from dataclasses import dataclass

@dataclass
class QueryData:
    """
    QueryData is a dataclass that contains the data needed to calculate the commission
    """
    sales_rep_name: str
    start_date: str
    end_date: str