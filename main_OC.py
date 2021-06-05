########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################### Alejandro de Miguel   ######################################################
##################### OpenCosmos challenge -- Mathematical Modelling & Simulation Challenge Project ####################
########################################################################################################################
########################################################################################################################
########################################################################################################################

#region HYPOTHESIS
# Solar panel opposite to nadir

# Solar flux is constant (negligible changes in distance wrt Sun or Sun activity)

# Perturbations not considered (oblateness, SRP, magnetosphere, airdrag...) when propagating the satellite orbit
# because the purpose is to study the power generated depending on the selected orbit, and adding perturbations
# would complicate this study
# Oblateness of Earth not considered (no regression of the nodes and advance of the perigee considered)
# SRP has not been modeled for example because we dont have any info about the satellite size or optic properties

# A solar panel at EOL (end-of-life) is considered (affects solar panel efficiency)

# Law of the effect of incident sun rays over solar panel efficiency: cos(theta), but there may be better models.
# source: https://www.cebrightfutures.org/learn/incident-angle-sunlight

# Solar rays arrive "straight", considering the sun sufficiently far away we can consider that all the
# solar rays arrive in the sun-earth direction (plane wavefront). Because the sun is so far from the earth, the
# angle between the earth-sun and satellite-sun is les than 0.02 deg even for GEO satellites

# include in the report the fact that solar rays inciding with angles bigger than 90 deg are not considered because
# even tho the satellite can be illuminated, the array is not facing towards the sun
#endregion

#region Import packages
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
#endregion

#region Import files
from kep2car import kep2car
from integrate_orbit import integrate_orbit
from JD import JD
from sun_position import sun_position
from lineofsight import lineofsight
from data_OC import seconds, minutes, hour, day, month, year
from data_OC import a, e, i, O, o, th, T
from data_OC import mu_earth, radius_earth
from data_OC import integrator, atol, rtol, integration_steps, t_i, t_f
from data_OC import power_max
#endregion

#region Compute sun's and satellite's position vector
jd0 = JD(year, month, day, hour, minutes, seconds)  # initial Julian day, to compute the sun's initial position
x0 = kep2car(a, e, i, O, o, th, mu_earth)  # initial satellite state vector
t = np.linspace(t_i, t_f, integration_steps)  # mission time vector

rr_s_vector = np.zeros((3, len(t)))
counter = 0
for s in t:
    jd = jd0 + s/3600/24
    lamda, epsilon, rr_s = sun_position(jd)
    rr_s_vector[0, counter] = rr_s[0]
    rr_s_vector[1, counter] = rr_s[1]
    rr_s_vector[2, counter] = rr_s[2]
    counter += 1

sol = solve_ivp(integrate_orbit, [0, t[-1]], x0, method=integrator, t_eval=t, args=(mu_earth,), rtol=rtol, atol=atol)
#endregion

#region Is satellite eclipsed or illuminated?
isilluminated_vector = np.zeros((len(t), 1))
theta_vector = np.zeros((len(t), 1))
power_generated_vector = np.zeros((len(t), 1))  # contains the power generated at each time
t_illum_vector = np.array([])  # contains the times when the satellite is illuminated
for i in range(len(t)):
    isilluminated, theta = lineofsight(rr_s_vector[:, i], sol.y[0:3, i])
    isilluminated_vector[i] = isilluminated
    theta_vector[i] = theta
    if isilluminated:
        t_illum_vector = np.append(t_illum_vector, t[i])  # to plot eclipsed/illuminated regions
        if 0 <= theta <= np.pi/2:
            power_generated_vector[i] = power_max * np.cos(theta)  # computes power depending on incidence angle
#endregion


#region PLOTS
fig1 = plt.figure(figsize=[8.4, 6.8])
ax1 = fig1.add_subplot(111, projection='3d')
plt.subplots_adjust(hspace=0.95)
ax1.plot(sol.y[0, :], sol.y[1, :], sol.y[2, :])
plt.title('Satellite orbit around the Earth')
ax1.set_xlabel('x-axis [km]')
ax1.set_ylabel('y-axis [km]')
ax1.set_zlabel('z-axis [km]')
plt.grid()


# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111, projection='3d')
# ax2.plot(rr_s_vector[0, :], rr_s_vector[1, :], rr_s_vector[2, :])
# plt.title('Sun orbit around the Earth')
# ax2.set_xlabel('x-axis [km]')
# ax2.set_ylabel('y-axis [km]')
# ax2.set_zlabel('z-axis [km]')
# plt.grid()


# fig3 = plt.figure()
# ax3 = fig3.add_subplot(111)
# r = np.array([])
# for i in range(len(t)):
#     aux = np.linalg.norm(sol.y[0:2, i])
#     r = np.append(r, aux)
# for i in t_illum_vector:
#     ax3.axvline(i, alpha=0.3, color='yellow')
# ax3.plot(t, r)
# plt.title('Distance of satellite wrt Earth')
# ax3.set_xlabel('Time [s]')
# ax3.set_ylabel('r [km]')
# plt.grid()


fig4 = plt.figure(figsize=[8.4, 6.8])
ax4_1 = fig4.add_subplot(313)
plt.subplots_adjust(hspace=0.95)
ax4_1.plot(t/T, theta_vector*180/np.pi)
ax4_1.title.set_text('Angle between sun-satellite position vectors over time')
ax4_1.set_xlabel('nº of orbital periods T')
ax4_1.set_ylabel('theta [deg]')
ax4_1.grid()
ax4_2 = fig4.add_subplot(312)
ax4_2.plot(t/T, power_generated_vector)
ax4_2.title.set_text('Power generated over time')
ax4_2.set_xlabel('nº of orbital periods T')
ax4_2.set_ylabel('Power generated [W]')
ax4_2.grid()
ax4_3 = fig4.add_subplot(311)
r = np.array([])
for i in range(len(t)):
    aux = np.linalg.norm(sol.y[0:3, i])
    r = np.append(r, aux)
for i in t_illum_vector/T:
    line = ax4_3.axvline(i, alpha=0.3, color='yellow')
ax4_3.plot(t/T, r)
ax4_3.title.set_text('Distance of satellite wrt Earth')
ax4_3.set_xlabel('nº of orbital periods T')
ax4_3.set_ylabel('r [km]')
ax4_3.legend([line], ['illuminated region'])
ax4_3.grid()


plt.show()
#endregion
