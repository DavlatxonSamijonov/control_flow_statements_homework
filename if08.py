def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    n = 57
    if n%2 == 1:
        a+= 2
    if n%2 == 0:
        a+= 1
    return a 
print ("two-digit odd number")