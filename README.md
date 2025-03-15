# Bisection Method

The **Bisection Method** is a numerical technique used for finding the root of a continuous function. This repository provides an implementation of the **Bisection Method** to approximate the root of a function `f(x) = 0` within a specified interval `[a, b]` and a given number of iterations `N`.

---

## Features

- **Root Approximation**: The function approximates the root of any continuous function `f(x) = 0` using the Bisection Method.
- **Flexible Interval**: You can specify the interval `[a, b]` where the root is located.
- **Iterations**: You can control the number of iterations `N` for the approximation, allowing for a balance between speed and precision.
- **Error Handling**: The method handles cases where the initial interval does not contain a root or if something goes wrong during the execution.

---

## Installation

You don’t need to install anything extra. The implementation is in plain Python, and you can run it in any Python environment.

1. Clone the repository:

```bash
git clone https://github.com/yourusername/bisection-method.git
```

2. Navigate to the directory:

```bash
cd bisection-method
```

---

## Usage

### Example Function

The method works for any continuous function. Here’s an example of using the Bisection Method to approximate the root of the function `f(x) = x^2 - x - 1`.

```python
def f(x):
    return x**2 - x - 1
```

### Bisection Method Implementation

```python
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
        elif f(a) * f(m) < 0:  # If midpoint is between point a and m
            b = m
        elif f(m) * f(b) < 0:  # If midpoint is between point m and b
            a = m
        else:
            print("Something went wrong.")
            return None

    # Return the midpoint of the final interval
    print(f"The boundary is from {a} to {b}")
    return (a + b) / 2
```

### Example Usage

```python
# Define the function
def f(x):
    return x**2 - x - 1

# Call the bisection method
result = bisection(f, 1, 2, 25)

# Output the result
if result is not None:
    print(f"Root approximation: {result}")
```

---

## Parameters

- **f**: The function for which the root is to be found. It should be a callable Python function.
- **a**: The left boundary of the interval. This value should be chosen such that the function changes sign between `a` and `b`.
- **b**: The right boundary of the interval.
- **N**: The maximum number of iterations to perform. More iterations lead to higher precision.

---

## Output

- If the Bisection Method finds the root within the specified interval and number of iterations, the approximation of the root will be printed.
- If the method detects that no root is present within the interval, it will print an error message and return `None`.
- If something goes wrong during the execution, the method will return `None` with a descriptive error message.

---

## Example Output

```bash
The boundary is from 1.6180305481319427 to 1.6180351427078247
Root approximation: 1.6180328454198837
```
