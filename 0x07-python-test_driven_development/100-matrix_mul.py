def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists, or if one element of those list of lists is not an integer or a float, or if m_a or m_b is not a rectangle (all ‘rows’ should be of the same size).
        ValueError: If m_a or m_b is empty (it means: = [] or = [[]]), or if m_a and m_b can’t be multiplied.

    Returns:
        list: The product matrix.
    """
    # Check that m_a and m_b are lists of lists
    if not isinstance(m_a, list) or not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check that m_a and m_b are not empty
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # Check that all elements in m_a and m_b are integers or floats
    for row in m_a + m_b:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_a should contain only integers or floats" \
                                "or m_b should contain only integers or floats")

    # Check that all rows in m_a and m_b have the same length
    if any(len(row) != len(m_a[0]) for row in m_a) \
            or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size" \
                        "or each row of m_b must be of the same size")

    # Check that the number of columns in matrix A is equal to the number of rows in matrix B
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply the matrices
    result = [[sum(a * b for a, b in zip(row, col)) \
               for col in zip(*m_b)] for row in m_a]

    return result
