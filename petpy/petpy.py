"""
Petrofysics equations
"""
def gardner(vp, alpha=310, beta=0.25):
    """
    Compute bulk density (in kg/m3) from vp (in m/s)
    """
    return alpha * vp**beta

def impedance(vp, rho):
    return vp * rho