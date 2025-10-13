# Joshua Evans - thejoshuaevans@gmail.com - 2025-10-12
# Lab 2a - Advanced Shipping
# From these instructions: https://lcc-cit.github.io/CS210-CourseMaterials/Labs/Lab02-RuleBasedSystems/GroupA/CS210_Lab02_Instructions_GroupA.html
# Requirements:
# 1. Write a set of rules. There should be at least 6. ✅
# 2. The rules will be designed for forward chaining. ✅
# 3. The rules for the system will be stored in a csv file. ✅
# 4. The program will load the contents of the csv file into a List of Dictionaries. ✅
# 5. The inference part of your program will implement forward chaining. ✅
# 6. User input and output should be separated from code that does inference. ✅

import csv, os

RULES_FILE_NAME = 'shipping_rules.csv'
SHIPPING_ZONES = ['A', 'B', 'C']

def generate_file_path(file_path: str) -> str:
    """
    Generate an absolute file path relative to this file - the entry point of this application. This
    allows the program to be run from any directory

    Args:
        file_path (str): The relative file path to convert to an absolute path
    Returns:
        out (str): The absolute file path
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, file_path)
    return os.path.realpath(file_path)

def read_csv(file_path: str) -> list[dict[str, str]]:
    """
    Reads a CSV file and returns its contents as a list of dictionaries. Each dictionary represents a row
    in the CSV file, with the keys being the column headers.

    Args:
        file_path (str): The path to the CSV file relative to this file.
    Returns:
        out (list[dict[str, str]]): The contents of the CSV file as a list of dictionaries.
    """
    data = []
    with open(generate_file_path(file_path)) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for item in row: # Strip the whitespace because it bothers me
                row[item] = row[item].strip()
            data.append(row)
    return data

def execute(statement:str, globals:dict, locals:dict):
    """
    Execute a statement defined in the shipping_rules.csv file

    Args:
        statement (str): The statement to run
        globals (dict): Global values to pass to the statement (cannot be changed)
        locals (dict): Local values to pass to the statement (can be changed)

    Returns:
        out: The result of the expression. For IF and AND statements, this should be a boolean
    """
    # Add a 'result' property to the local values if it does not exist, so that we can
    # extract the result of the statement
    if 'result' not in locals:
        locals['result'] = None

    # Ensure that there are no "builtins" available to the statement as a basic (but ultimately
    # inadequate) safety measure
    globals = globals | {'__builtins__': {}}

    # Perform the execution...
    #! WARNING: The use of `exec` is generally discouraged, and is an advanced technique
    #* `exec` is considered forbidden black magic, and for very good reason. Without any validation,
    #* it would be possible for a bad actor to execute ANY command on your machine by manipulating the
    #* input file. In a real-world case, if there is no other option, the input statement for `exec`
    #* should always be thoroughly validated to ensure it is not dangerous and should always come from
    #* a trusted source

    # Forbidden black magic is powerful despite its dangers... and `exec` allows us to do really cool
    # things like put python statements in our inputs for significantly more advanced functionality

    # Python allows us to pass dictionaries to the `exec` function that will be applied to the
    # statement being run. The "globals" will be applied as global variables and cannot be altered. The
    # "locals" will be applied to the local scope, and can be changed by the statement. So, we run the
    # statement and set it to a "result" value that we can then extract from the local variables
    exec(f'result = {statement}', globals, locals)

    return locals['result']

def calculate_shipping_cost(weight_kg: float, from_zone: str, to_zone: str) -> dict[str, float]:
    """
    Generates the cost of shipping a parcel according to its weight and shipping zones. Includes tax
    calculation based on sending zone

    Args:
        weight_kg (float): The weight of the parcel in kilograms
        from_zone (str): The shipping zone the package is being sent from
        to_zone (str): The shipping zone the package is being delivered to

    Returns:
        out (dict[str, float]): A package of shipping cost data
    """
    # Get the rules
    rules = read_csv(RULES_FILE_NAME)

    # Data that will not be changed (inputs)
    global_data = {
        'weight_kg': weight_kg,
        'from_zone': from_zone,
        'to_zone': to_zone,
    }

    # Data that will be changed (outputs)
    local_data = {
        'cost': 0.0,
        'tax': 0.0,
    }

    # Process all the rules
    for rule in rules:
        # Process the IF block
        if execute(rule['IF'], global_data, local_data) != True:
            # This "IF" statement is not true, skip to the next rule
            continue

        # Process the AND block if it is present
        if rule['AND']:
            if execute(rule['AND'], global_data, local_data) != True:
                # This "AND" statement is not true, skip to the next rule
                continue

        # All statements pass, process the THEN block
        execute(rule['THEN'], global_data, local_data)

        # If this is a GOAL, break the loop - there is no more processing to do
        if rule['GOAL'].lower() == 'true':
            break

    result = {
        'cost': local_data['cost'],
        'tax': local_data['tax'],
        'total_cost': local_data['cost'] * (1 + local_data['tax']),
    }
    return result

def print_error(err:str) -> None:
    """Simple helper prints an error string with conspicuous decorations"""
    print(f'\n===== Error: {err} =====\n')

def get_weight_kg() -> float:
    """
    Perform input validation getting the parcel's weight in kilograms

    Returns:
        float: The parcel's weight in kilograms
    """
    while True:
        try:
            user_input = float(input('Enter the weight of the package in kg: ').strip())
            if (user_input <= 0):
                print_error('Please enter a value greater than 0')
                continue

            return user_input
        except ValueError:
            print_error('Please enter a valid decimal number')

def get_from_zone() -> str:
    """
    Perform input validation getting the zone the package is being sent from

    Returns:
        str: The shipping zone
    """
    while True:
        user_input = input(f'Enter the shipping zone the package is being sent FROM ({SHIPPING_ZONES}): ').strip().upper()
        if user_input not in SHIPPING_ZONES:
            print_error(f'Please enter a valid shipping zone (choose from {SHIPPING_ZONES})')
            continue

        return user_input

def get_to_zone() -> str:
    """
    Perform input validation getting the zone the package is being delivered to

    Returns:
        str: The shipping zone
    """
    while True:
        user_input = input(f'Enter the shipping zone the package is being delivered TO ({SHIPPING_ZONES}): ').strip().upper()
        if user_input not in SHIPPING_ZONES:
            print_error(f'Please enter a valid shipping zone (choose from {SHIPPING_ZONES})')
            continue

        return user_input

def main():
    print('Thank you for choosing the Super Shipping Calculator 9000!')
    weight_kg = get_weight_kg()
    from_zone = get_from_zone()
    to_zone = get_to_zone()

    print('\nCalculating shipping cost...\n')
    cost, tax, total_cost = calculate_shipping_cost(weight_kg, from_zone, to_zone).values()

    print(f'Final shipping cost: ${total_cost:.2f} (${cost:.2f} * {tax*100}% tax)')

if __name__ == "__main__":
    main()
