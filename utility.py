# Module with utility functions

# Constants
EPS = 1e-5

# Function to check if two values are approximately equal
# in: first, second - values to compare
#     eps - error
def approxEqual(first, second, eps = EPS):
    return abs(first - second) < eps
