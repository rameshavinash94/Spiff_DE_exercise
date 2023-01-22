from CommisionStrategyFactory import CommissionStrategyFactory
from UserQuerydata import QueryData

class CalcuateCommission:
    """
    CalcuateCommission is a class that calculates the commission
    """
    def __init__(self, commissionStrategyFactory: CommissionStrategyFactory):
        self._commissionStrategyFactory = commissionStrategyFactory

    def CalculateCommission(self, data:QueryData,commissionType: str) -> float:
        """
        CalculateCommission is a method that calculates the commission

        Args:
            data (QueryData): QueryData is a dataclass that contains the data needed to calculate the commission
            commissionType (str): The commission type

        Returns:
            float: The total commission
        """
        strategy = self._commissionStrategyFactory.GetCommissionStrategy(commissionType)
        return strategy.CalculateCommission(data)