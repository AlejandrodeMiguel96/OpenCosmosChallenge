# This file contains the function that computes the Julian day number

import numpy as np


def JD(year, month, day, hour, minutes, seconds):
    """
    Computes the Julian day number for any year between 1900 and 2100.
    Reference: H.Curtis
    :param year: range 1901 - 2099
    :param month: range 1 - 12
    :param day: range 1 - 31
    :param hour: range 0 - 23
    :param minutes: range 0 - 59
    :param seconds: range 0 - 59
    :return:
        j0: Julian day at 0 hr UT (Universal time)
    """
    if 1901 <= year <= 2099 and 1 <= month <= 12 and 1 <= day <= 31 and 0 <= hour <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
        j0 = 367 * year - np.fix(7*(year + np.fix((month+9)/12))/4) + np.fix(275*month/9) + day + 1721013.5
        UT = hour + minutes/60 + seconds/3600
        j0 += UT/24
        return j0
    else:
        # would be better to raise an error but it does the trick for preliminar testing
        print('ERROR! ERROR! ERROR! ERROR! ERROR! ERROR! ERROR! ERROR! ERROR! ERROR! ERROR! IN FILE J0.PY, FUNCTION JO')
        return 0


