from CommissionStrategyInterface import CommissionStrategy
from CommisionStrategies import FixedCommissionStrategy

class CommissionStrategyFactory:
    """
    CommissionStrategyFactory is a class that creates a commission strategy
    """
    def GetCommissionStrategy(self,commissionType: str="Fixed") -> CommissionStrategy:
        """
        GetCommissionStrategy is a method that creates a commission strategy

        Args:
            commissionType (str, optional): Defaults to "Fixed".

        Raises:
            Exception: Invalid commission type

        Returns:
            CommissionStrategy: A commission strategy
        """
        if commissionType == "Fixed":
            return FixedCommissionStrategy()
        else:
            raise Exception("Invalid commission type")
