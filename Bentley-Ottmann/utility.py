# Module with utility functions

# Constants
EPS = 1e-10

# Function to check if two values are approximately equal
# In: first, second - values to compare
#     eps - error
def approxEqual(first, second, eps = EPS):
    return abs(first - second) < eps
