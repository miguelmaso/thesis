import numpy as np
import matplotlib.pyplot as plt

def _InvH(h):
    return np.sqrt(2.0) * max(h, 0.0) / np.sqrt(h**4 + max(h**4, 1.0))
InvH = np.vectorize(_InvH)

def _WetFraction(h):
    return h * InvH(h)
WetFraction = np.vectorize(_WetFraction)

x = np.linspace(0, 5, 200)
h_inv = InvH(x)
wet_f = WetFraction(x)

fig, ax = plt.subplots(nrows=1, ncols=2, sharey=True)
fig.set_size_inches(7,4)
ax[0].plot(x, h_inv)
ax[1].plot(x, wet_f)
ax[0].plot([1,1], [0,1], color='k', linewidth=1, linestyle='dashed')
ax[1].plot([1,1], [0,1], color='k', linewidth=1, linestyle='dashed')
ax[0].set_title('Dimensionless inverse height')
ax[1].set_title('Wet fraction')
ax[0].set_xlabel('$h/\epsilon$')
ax[1].set_xlabel('$h/\epsilon$')
fig.tight_layout()
plt.show()
