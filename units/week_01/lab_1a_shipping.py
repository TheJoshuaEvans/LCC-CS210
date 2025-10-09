# Joshua Evans - 2025-10-02
# Lab 1a part 1 - Shipping
# Based off of this JS program: https://lcc-cit.github.io/CS210-CourseMaterials/Labs/Lab01-Python/GroupA/shippingCalculator.js
# (It's supposed to just be a translation but I got a bit carried away lol)

shipping_values = {
    "A": {
        "min": 10.00,
        "med": 15.00,
        "max": 20.00,
    },
    "B": {
        "min": 15.00,
        "med": 20.00,
        "max": 25.00,
    },
    "C": {
        "min": 20.00,
        "med": 25.00,
        "max": 30.00,
    },
}
"""All of the possible shipping values"""

def determine_shipping_size(weight_kg: float) -> str:
    """
    Determine the size of an item based on it's weight in kilograms

    Parameters:
        weight_kg (float): The weight of the parcel in kilograms
    """
    if weight_kg <= 5: return "min"
    elif weight_kg <= 10: return "med"
    else: return "max"

def calculate_shipping_cost(weight_kg: float, zone: str) -> float|None:
    """
    Calculate the shipping cost of a parcel based on it's weight and shipping zone. If an invalid shipping
    zone is provided a message will be printed and None will be returned

    Parameters:
        weight_kg (float): The weight of the parcel in kilograms
        zone ("A"|"B"|"C"): The shipping zone
    """

    # Make sure zone is uppercase
    zone = zone.upper()

    print("\n--- Shipping Cost Check ---")
    print(f"Package Details: {weight_kg} kg to Zone {zone}")

    # Check if the zone is valid
    if zone not in shipping_values:
        print("Error: Invalid shipping zone specified.")
        return None

    cost = shipping_values[zone][(determine_shipping_size(weight_kg))]

    print(f"Calculated Shipping Cost: {cost:.2f}")
    print(f"----------------------------")

    return cost
