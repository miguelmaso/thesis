import numpy as np
import matplotlib.pyplot as plt
from KratosMultiphysics.ShallowWaterApplication.utilities.wave_theory_utilities import BoussinesqTheory, LinearTheory, ShallowTheory

depth = 1.0
amplitude = 0.1

b1 = BoussinesqTheory(depth)
b2 = BoussinesqTheory(depth)
b3 = BoussinesqTheory(depth)
b4 = BoussinesqTheory(depth)
b5 = BoussinesqTheory(depth)
l = LinearTheory(depth)
s = ShallowTheory(depth)

b1.alpha = 0.0
b2.alpha = -1.0/3.0
b3.alpha = -0.390
b4.alpha = -2.0/5.0
b5.alpha = -0.5

kh = np.linspace(.1, 5, 100)

b1_values = []
b2_values = []
b3_values = []
b4_values = []
b5_values = []
s_values = []

for wavenum in kh:
    c = l._PhaseSpeed(wavenum)
    b1_values.append(b1._PhaseSpeed(wavenum) / c)
    b2_values.append(b2._PhaseSpeed(wavenum) / c)
    b3_values.append(b3._PhaseSpeed(wavenum) / c)
    b4_values.append(b4._PhaseSpeed(wavenum) / c)
    b5_values.append(b5._PhaseSpeed(wavenum) / c)
    s_values.append(s._PhaseSpeed(wavenum) / c)


plt.plot(kh, b1_values, color='darkblue', alpha=0.3, label=r'$\beta=0$')
plt.plot(kh, b2_values, color='darkblue', alpha=0.4, label=r'$\beta=-0.423$')
plt.plot(kh, b3_values, color='darkblue', alpha=0.5, label=r'$\beta=-0.531$')
plt.plot(kh, b4_values, color='darkblue', alpha=0.7, label=r'$\beta=-0.553$')
plt.plot(kh, b5_values, color='darkblue', alpha=0.8, label=r'$\beta=-1$')
plt.plot(kh, s_values, color='darkcyan', linestyle='dashed', label=r'$c^2=gh$')
plt.axvspan(0.3, 3, facecolor='gray', alpha=0.2)
plt.text(0.1, 0.5, 'shallow water', color='gray')
plt.text(0.45, 0.5, 'intermediate water', color='gray')
plt.xlabel(r'$kh$')
plt.ylabel(r'$c/c_{Airy}$')
plt.ylim([0.3, 2.1])
plt.xscale('log')
plt.legend()
plt.show()
