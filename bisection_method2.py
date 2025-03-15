def bisection(f, a, b, N):
    """
    Approximates a root of the function f(x) = 0 using the Bisection Method.

    Parameters:
    f (function): A callable function for which the root is to be found.
    a (float): The starting point of the interval [a, b].
    b (float): The ending point of the interval [a, b].
    N (int): The number of iterations to perform.

    Returns:
    float: Approximation of the root, or None if the method fails.
    """
    # Check if the initial interval is valid
    if f(a) * f(b) >= 0:
        print("No roots present: f(a) * f(b) >= 0")
        return None

    for i in range(N):
        # Compute the midpoint
        m = (a + b) / 2

        # Check if the midpoint is a root
        if f(m) == 0:
            return m

        # Determine the new interval
        elif f(a) * f(m) < 0: #If midpoint is in between point a & m
            b = m
        elif f(m) * f(b) < 0: #If midpoint is in between point m & b
            a = m
        else:
            print("Something went wrong.")
            return None

    # Return the midpoint of the final interval
    print(f"The boundary is from {a} to {b}")
    return (a + b) / 2


# Example usage
def f(x):
    return (x**2 - x - 1)
result = bisection(f, 1, 2, 25)
if result is not None:
    print(f"Root approximation: {result}")
