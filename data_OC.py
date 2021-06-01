# File containing the data constants of the problem
import numpy as np


#region Universal constants
mu_earth = 398600  # [km^3/s^2] Gravitational earth parameter.
radius_earth = 6378  # [km] Radius of the earth.
AU = 149597870.691  # [km] Astronomical unit
solar_constant = 1367  # [W/m^2] Average flux density to LEO. Data from H.Curtis
#endregion

#region 3U cubesat solar panels
# SOLAR PANELS DATA: http://propagation.ece.gatech.edu/ECE6390/project/Sum2015/team3/PowerSystem.html
solar_panel_area = 30*10 / 1e4  # [m^2] size of solar panels
cell_perc = 90/100  # [-] percentage of the panel covered by cells
cell_area = solar_panel_area * cell_perc  # [m^2] area filled by solar panel cells
cell_efficiency_BOL = 29/100  # [-] efficiency of the solar cells at beginning of life (BOL)
cell_efficiency_EOL = 87/100  # [-] efficiency of the solar cells at end of life (EOL, 10-15 years)
cell_efficiency = cell_efficiency_BOL * cell_efficiency_EOL  # [-] cell efficiency of cell at EOL
power_max = solar_constant * cell_efficiency * cell_area  # [W] Maximum obtainable power from the solar array
#endregion


#region Time of simulation
# Specify the initial date of the simulation
year = 2013
month = 7
day = 25
hour = 8
minutes = 0
seconds = 0
#endregion

#region Orbit data
# Example orbit
a = 6378+758.63  # [km] Semi-major axis
e = 0.05  # [-] Eccentricity
i = 98.43 * np.pi/180  # [rad] Inclination
O = 270 * np.pi/180  # [rad] Right ascension of the ascending node RAAN
o = 45 * np.pi/180  # [rad] Argument of the perigee
th = 230 * np.pi/180  # [rad] True anomaly (theta)

# Molniya orbit (Wikipedia)
# a = 26600  # [km] Semi-major axis
# e = 0.74  # [-] Eccentricity
# i = 63.4 * np.pi/180  # [rad] Inclination
# O = 90 * np.pi/180  # [rad] Right ascension of the ascending node RAAN
# o = 270 * np.pi/180  # [rad] Argument of the perigee
# th = 0 * np.pi/180  # [rad] True anomaly (theta)

# Curtis, example 4.12
# a = 83500  # [km] Semi-major axis
# e = 0.1976  # [-] Eccentricity
# i = 60 * np.pi/180  # [rad] Inclination
# O = 270 * np.pi/180  # [rad] Right ascension of the ascending node RAAN
# o = 45 * np.pi/180  # [rad] Argument of the perigee
# th = 230 * np.pi/180  # [rad] True anomaly (theta)

T = 2*np.pi*np.sqrt(a**3/mu_earth)  # [s] Orbital period
#endregion

#region Integrator values
atol = 1e-12  # Absolute integrator tolerance. Default is set to 1e-6
rtol = 1e-9  # Relative integrator tolerance. Default is set to 1e-3
integrator = 'DOP853'  # integrator chosen (e.g 'DOP853', 'Radau', 'LSODA', 'RK45')
integration_steps = 1000  # Number of integration steps
t_i = 0  # [s] initial simulation time
t_f = 2*T  # [s] final simulation time
#endregion




