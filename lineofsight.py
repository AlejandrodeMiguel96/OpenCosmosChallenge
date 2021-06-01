# This file contains the function to compute if a satellite is in eclipse wrt Earth

import numpy as np
from data_OC import radius_earth


def lineofsight(rr_sat, rr_sun):
    """
    Computes if a satellite is iluminated by the Sun or in the Earth's shadow
    :param rr_sat: [km] satellite position vector in ECI (wrt Earth)
    :param rr_sun: [km] sun position vector in ECI (wrt Earth)
    :return:
        [bool]
        True: it is in line of sight and illuminated
        False: it is NOT in line of sight NOR illuminated
        theta: [rad] angle between sun's and satellite's position vectors
    """
    RE = radius_earth  # [km] Earth's radius
    rsat = np.linalg.norm(rr_sat)  # magnitude of Earth-satellite vector
    rsun = np.linalg.norm(rr_sun)  # magnitude of Earth-Sun vector

    # Angle between sun-satellite
    theta = np.arccos(np.dot(rr_sat, rr_sun)/rsat/rsun)

    # Angle between satellite-radial to tangency point of satellite-earth
    theta_sat = np.arccos(RE/rsat)

    # Angle between sun-radial to tangency point of sun-earth
    theta_sun = np.arccos(RE/rsun)

    if theta_sat + theta_sun <= theta:
        illuminated = False
    else:
        illuminated = True

    return illuminated, theta




