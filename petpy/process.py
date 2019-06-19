"""
Processing utilities
"""
import numpy as np

def smooth_curve(curve, length):
    """
    Smooth a curve with boxcar of length elemnets
    """
    boxcar = np.ones(length)/length
    return np.convolve(boxcar, curve, mode='same')