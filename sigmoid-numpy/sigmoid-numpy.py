import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    input = np.array(x)
    return ( 1 / (1 + np.exp(-input)) )