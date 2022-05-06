__all__ = ['normalize']

import numpy as np

def normalize(data:np.ndarray):
    """Function normalizes the given input

    Parameters
    ----------
    data : np.ndarray
      input data

    Returns
    -------
    np.ndarray
      normalized data
    """
    return ((data - np.min(data)) / (np.max(data) - np.min(data)))

