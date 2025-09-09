

def compute_linear_range(start, end, m=2, b=3):
    """
    Computes y = mx + b for x in range [start, end].

    Args:
        start (int): Starting value of x.
        end (int): Ending value of x.
        m (float): Slope. Default is 2.
        b (float): Intercept. Default is 3.

    Returns:
        List[Tuple[int, float]]: List of (x, y) tuples.
    """
    if start > end:
        raise ValueError("Start must be less than or equal to end.")

    return [(x, m * x + b) for x in range(start, end + 1)]
