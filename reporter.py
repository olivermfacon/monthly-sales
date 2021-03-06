# reporter.py

import pandas 

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

print("READING GRADEBOOK CSV FILE...")

csv_filepath = "/Users/oliver/Documents/GitHub/monthly-sales/Data/gradebook.csv"
grades = pandas.read_csv(csv_filepath)

print("GRADES:", type(grades))
# print(dir(grades))

print(grades.tail())