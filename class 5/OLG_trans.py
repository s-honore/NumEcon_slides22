# a. import
import ipywidgets as widgets
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np


def transition(k,alpha,rho,n):
    """
    Returns:
    k1(float) capital in the next period
    
    Args:
    k (float): Initial stock of capital
    alpha (float): Capital income share.
    rho (float): Timepreference parameter
    n (float): Population growth
    
    output: 
    Computes the wage rate, optimal savings and capital in next period. 
    
    """
    # Raise ValueErrors
    if n>1:
        raise ValueError("Population growth cannot exceed 1")
    if alpha>1: 
        raise ValueError("Capital income share cannot exceed 1")
    if rho < 0: 
        raise ValueError("Timepreference cannot be a negative number")
    
    w = k**alpha * (1-alpha) #wage rate
    s = w / (rho+2) #optimal savings
    k1 = s / (n+1) #capital in the next period
    return k1

def transition_curve(alpha,rho,n,T=1000,k_min=1e-20,k_max=6):
    """
    Returns:
    k_1(array): Array of capital in period 1
    k_2(array): Array of capital in period 2
    
    Args:
    alpha (float): Capital income share
    rho (float): Timepreference parameter
    n (float): Population growth
    T (int): Number of periods. Default 1000 periods.
    k_min (float): Minimum capital value. Default 1e-20.
    k_max (float): Maximum capital value. Default 6.
    
    output: 
    For every value of capital computes the value of capital in the next period using the transition equation. 
    """
    
    if n>1:
        raise ValueError("Population growth cannot exceed 1")
    if alpha>1: 
        raise ValueError("Capital income share cannot exceed 1")
    if rho < 0: 
        raise ValueError("Timepreference cannot be a negative number")
    
    #grids
    k_1 = np.linspace(k_min,k_max,T)
    k_1 = np.linspace(1e-20,6,T)
    k_2 = np.empty(T)
    
    #construct array of "tomorrows" capital
    for i,k in enumerate(k_1):
        k_plus = transition(k,alpha,rho,n)
        k_2[i] = k_plus
        
    return k_1, k_2