from negmas import LinearUtilityFunction

from .indneg import IndependentNegotiationsAgent

__all__ = ["BuyCheapSellExpensiveAgent"]


class BuyCheapSellExpensiveAgent(IndependentNegotiationsAgent):
    """An agent that tries to buy cheap and sell expensive but does not care about production scheduling."""

    def create_ufun(self, is_seller: bool, issues=None, outcomes=None):
        if is_seller:
            return LinearUtilityFunction(
                {"unit_price": 1, "quantity": 0.1, "time": 0.1}
            )
        return LinearUtilityFunction({"unit_price": -1, "quantity": 0.1, "time": -0.1})
