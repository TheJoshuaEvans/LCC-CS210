from enum import Enum

class CoffeeSize(Enum):
  """The size of a coffee"""
  small = 3.00
  """12 oz"""
  medium = 4.00
  """16 oz"""
  large = 5.50
  """20 oz"""

class CoffeeMilk(Enum):
  """The type of milk used in a coffee"""
  dairy = 0.00
  """Standard dairy milk"""
  oat = 0.75
  """Organic oat milk"""
  almond = 0.50
  """Almond milk"""
  science = 0.75
  """Lactose free dairy milk"""

def price_coffee(size: CoffeeSize|str, milk: CoffeeMilk|str = CoffeeMilk.dairy) -> float:
    """Determine the price of a coffee based on the provided parameters

    Parameters:
        size (CoffeeSize | str): The size of the coffee
        milk (CoffeeMilk | str, optional): The type of milk to use. Defaults to dairy

    Returns:
        result (float): The price of the coffee
    """

    # Instead else-if blocks, enums are used to simplify internal calculations - but if strings
    # were provided to the function (which is how the unit tests work) they need to be converted
    # into the correct enum. This can all be done dynamically! :D
    size_str = size.name if isinstance(size, CoffeeSize) else size
    _size = CoffeeSize[size_str]

    milk_str = milk.name if isinstance(milk, CoffeeMilk) else milk
    _milk = CoffeeMilk[milk_str]

    return _size.value + _milk.value

if __name__ == '__main__':
    coffee_size = CoffeeSize.small
    coffee_milk = CoffeeMilk.oat

    print(f"Coffee cost: ${price_coffee(coffee_size, coffee_milk):.2f}")
