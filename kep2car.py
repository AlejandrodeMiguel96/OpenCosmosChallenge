# File containing the function to convert from keplerian elements to cartesian coordinates
import numpy as np


def kep2car(a, e, i, O, o, th, mu):
    """
    Converts the Keplerian elements to cartesian coordinates.
    :param a: semi-major axis [km]
    :param e: eccentricity []
    :param i: inclination [rad]
    :param O: RAAN (right ascension of the ascending node) [rad]
    :param o: argument of the perigee [rad]
    :param th: true anomaly [rad]
    :param mu: gravitational parameter [km^3/s^2]
    :return: r,v [km, km/s] position and velocity vectors
    """
    R3_O = np.array([
        [np.cos(O), np.sin(O), 0],
        [-np.sin(O), np.cos(O), 0],
        [0, 0, 1]
    ])  # rotation matrix about the z-axis through the angle O
    R1_i = np.array([
        [1, 0, 0],
        [0, np.cos(i), np.sin(i)],
        [0, -np.sin(i), np.cos(i)]
    ])  # rotation matrix about the x-axis through the angle i
    R3_o = np.array([
        [np.cos(o), np.sin(o), 0],
        [-np.sin(o), np.cos(o), 0],
        [0, 0, 1]
    ])  # rotation matrix about the z-axis through the angle o

    h = np.sqrt(a*mu*(1-e**2))
    rp = (h**2/mu) * (1/(1+e*np.cos(th))) * (np.cos(th)*np.array([[1],[0],[0]]) + np.sin(th)*np.array([[0],[1],[0]]))
    vp = (mu/h) * (-np.sin(th)*np.array([[1],[0],[0]]) + (e+np.cos(th))*np.array([[0],[1],[0]]))
    Q_pX = np.linalg.inv(np.dot(np.dot(R3_o, R1_i), R3_O))
    r = np.dot(Q_pX, rp)
    v = np.dot(Q_pX, vp)
    return np.append(r, v)










