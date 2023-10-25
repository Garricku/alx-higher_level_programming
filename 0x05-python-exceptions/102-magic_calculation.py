def magic_calculation(a, b):
    """
    This function replicates the behavior of the given Python bytecode.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The result of the calculation.
    """
    result = 0
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception("Too far")
            result += a ** b / i
        except Exception:
            result += b
            continue
    return result
