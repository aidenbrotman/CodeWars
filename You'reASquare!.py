import math
def is_square(n):
    if n >= 0:
        sqrt_n = round(math.sqrt(n))
        return True if sqrt_n**2 == n else False
    else:
        return False



is_square(0)