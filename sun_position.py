# This file contains the function that returns the Sun's geocentric position at a given epoch

import numpy as np
from data_OC import AU

def sun_position(jd):
    """
    This functino computes the geocentric equatorial position vector of the sun, given a Julian date.
    Reference: H.Curtis
    :param jd: julian date
    :return:
        lambda: [deg] apparent ecliptic longitude
        epsilon: [deg] obliquity of the ecliptic
        rr_s: [km] geocentric position vector
    """
    n = jd - 2451545  # [days] Julian days since J2000
    cy = n/36525  # [centuries] Julian centuries since J2000

    # Mean anomaly (deg)
    M = 357.529 + 0.98560023*n
    M = M % 360  # remainder of the division

    # Mean longitude (deg)
    L = 280.459 + 0.98564736*n
    L = L % 360

    # Apparent ecliptic longitude (deg)
    lamda = L + 1.915 * np.sin(M*np.pi/180) + 0.02*np.sin(2*M*np.pi/180)
    lamda = lamda % 360

    # Obliquity of the ecliptic (deg)
    epsilon = 23.439 - 0.000000356*n

    # Unit vector from earth to sun
    u = np.array([
        [np.cos(lamda*np.pi/180)],
        [np.sin(lamda*np.pi/180)*np.cos(epsilon*np.pi/180)],
        [np.sin(lamda*np.pi/180)*np.sin(epsilon*np.pi/180)]
    ])

    # Distance from earth to sun (km)
    r_s = (1.00014 - 0.01671 * np.cos(M*np.pi/180) - 0.00014*np.cos(2*M*np.pi/180)) * AU

    # Geocentric position vector (km)
    rr_s = r_s * u

    return lamda, epsilon, rr_s












