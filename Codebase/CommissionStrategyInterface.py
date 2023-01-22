from abc import ABC, abstractmethod
from UserQuerydata  import QueryData

class CommissionStrategy(ABC):
    """
    CommissionStrategy is an abstract class that defines the CalculateCommission method
    """

    @abstractmethod
    def CalculateCommission(self,data:QueryData) -> float:
        """
        CalculateCommission is an abstract method that calculates the commission

        Args:
            data (QueryData): QueryData is a dataclass that contains the data needed to calculate the commission

        Returns:
            float: The total commission
        """
        pass