# File containing the function to integrate an orbit
import numpy as np


def integrate_orbit(t, x, mu):
    """
    Propagates the orbit given its initial state vector and the gravitational parameter.
    :param t:
    :param x: initial state vector [km, km/s]
    :param mu: gravitational parameter [km^3/s^2]
    :return: xdot [km, km/s]
    """
    r_norm = np.linalg.norm([x[0], x[1], x[2]])
    return [
        x[3],
        x[4],
        x[5],
        -mu/r_norm**3 * x[0],
        -mu/r_norm**3 * x[1],
        -mu/r_norm**3 * x[2]
    ]



