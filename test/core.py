__all__ = ['normalize', 'normalize2', 'fun', 'fun2', 'fun3']

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

def normalize2(data:np.ndarray):
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

def fun(x:int, y:int, z:int):
    """adds number in the args

    Parameters
    ----------
    x : int
      input data
    y : int
      input data
    z : int
      input data

    Returns
    -------
    int
      sum
    """
    return ((x + y) + z)

def fun2(x:int, y:int, z:int):
    """adds number in the args

    Parameters
    ----------
    x : int
      input data
    y : int
      input data
    z : int
      input data

    Returns
    -------
    int
      sum
    """
    return ((x + y) + z)

def fun3(x:int, y:int, z:int):
    """adds number in the args

    Parameters
    ----------
    x : int
      input data
    y : int
      input data
    z : int
      input data

    Returns
    -------
    int
      sum
    """
    return ((x + y) + z)

