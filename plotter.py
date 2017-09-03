import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0,2*np.pi, 40)

# Position Equation

def ry(t):
	
    return t * np.sin(t)

# Velocity Vector

def vy(t):

    return np.sin(t) + t*np.cos(t)

# Acceleration Vector

def ay(t):
    return 2*np.cos(t) - t*np.sin(t)





