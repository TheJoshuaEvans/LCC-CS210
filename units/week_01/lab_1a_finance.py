# Joshua Evans - 2025-10-02
# Lab 1a part 2 - Finance

import numbers
from typing import overload, Union

advice_matrix = {
    "short": {
        "low": "High-Yield Savings Account",
        "high": "Short-Term Corporate Bonds",
    },
    "long": {
        "low": "Government Bonds/Index Fund",
        "high": "Diversified Stock Portfolio",
    },
}
"""Dictionary connecting time horizon, risk tolerance, and final advice strings"""

@overload
def generate_financial_advice(horizon:float, tolerance:str) -> str:
    """
    Takes an investment horizon (in years) and a risk tolerance level (low or high) and recommends
    an investment product suitable to the provided parameters. Throws a ValueError if invalid parameters
    are provided

    (Note: Not financial advice)

    Parameters:
        horizon (float): The desired time horizon in years
        risk ("low"|"high"): The acceptable risk profile
    """
...

@overload
def generate_financial_advice(horizon:str, tolerance:str) -> str:
    """
    Takes an investment horizon (short or long term) and a risk tolerance level (low or high) and recommends
    an investment product suitable to the provided parameters. Throws a ValueError if invalid parameters
    are provided

    (Note: Not financial advice)

    Parameters:
        horizon ("short"|"long"): The desired time horizon
        risk ("low"|"high"): The acceptable risk profile
    """
...

def generate_financial_advice(horizon:str|float, tolerance:str) -> str:
    if isinstance(horizon, (int, float)):
        # Convert numeric time horizon into a defined category
        if (horizon < 0):
            raise ValueError(f"Invalid time horizon. Time must be positive. Received {horizon}")

        horizon = "short" if horizon < 5 else "long"

    if horizon not in advice_matrix:
        raise ValueError(f"Invalid time horizon. Expected 'short' or 'long'. Received {horizon}")

    if tolerance not in advice_matrix[horizon]:
        raise ValueError(f"Invalid risk tolerance. Expected 'high' or 'low'. Received {tolerance}")

    return advice_matrix[horizon][tolerance]
