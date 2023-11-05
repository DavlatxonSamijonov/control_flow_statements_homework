def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    n = 0
    if a > 0:
       n += 1
    if a < 0:
        n += 1
    if a == 0:
        n += 1
    return a 
print ("positive odd number")
print ("negative even number")