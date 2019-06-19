from petpy import gardner
import numpy as np

EPSILON = 1e-6  # global variable

def test_gardner():
    rhob = gardner(2000)  # 2073
    assert np.isclose(rhob, 2073.09494543)