import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
sys.path.append('/graphics/')

time = 0.5

b_max = 6.0
start = 60
end = 100

name = 'graphics/output_file.dat'

def ReadDataFrame(file_name):
    rows = 5
    df = pd.read_csv(file_name, sep='\s+', skiprows=5)
    df.columns = df.columns.str.replace('[#,@,&]', '', regex=True)
    df.sort_values('position', inplace=True)
    return df

def SmoothFunction(position):
    if position > start:
        smooth_function = np.expm1(((position - start)/(end - start))**3) / np.expm1(1.0)
    else:
        smooth_function = 0.0
    return b_max * smooth_function

AbsorbingCoefficient = np.vectorize(SmoothFunction)

df = ReadDataFrame(name)

Beta = AbsorbingCoefficient(df['position'].to_numpy())
df['Beta'] = Beta


fig, axes = plt.subplots(nrows=2, sharex=True)
plt.rcParams['lines.linewidth'] = 2
axes0 = axes[0].twinx()
axes1 = axes[1].twinx()
axes[0].set_zorder(axes0.get_zorder()+1)
axes[1].set_zorder(axes1.get_zorder()+1)
axes[0].patch.set_visible(False)
axes[1].patch.set_visible(False)


df.plot(x='position', y='FREE_SURFACE_ELEVATION', ax=axes[0])
df.plot(x='position', y='MOMENTUM_X', label='DISCHARGE', ax=axes[1], color='red')
axes0.fill_between([start, end], -b_max, b_max, color='lightgray')
axes1.fill_between([start, end], -b_max, b_max, color='lightgray')
axes0.plot([0, end], [0, 0], linewidth=1, color='gray', linestyle='solid')
axes1.plot([0, end], [0, 0], linewidth=1, color='gray', linestyle='solid')
# df.plot(x='position', y='Beta', label='DAMPING_COEFFICIENT', ax=axes0, linewidth=1, color='black', linestyle='solid')
df.plot(x='position', y='Beta', label='DAMPING_COEFFICIENT', ax=axes1, linewidth=1, color='black', linestyle='solid')


axes[0].set_ylabel('$[m]$')
axes[1].set_ylabel('$[m^2/s]$')
axes[1].set_xlabel('Position $[m]$')
axes0.set_ylim([-b_max, b_max])
axes1.set_ylim([-b_max, b_max])


axes0.get_yaxis().set_visible(False)
# line1, label1 = axes[0].get_legend_handles_labels()
# line2, label2 = axes0.get_legend_handles_labels()
# axes[0].legend(line1 + line2, label1 + label2)
# axes0.legend().remove()
line1, label1 = axes[1].get_legend_handles_labels()
line2, label2 = axes1.get_legend_handles_labels()
axes[1].legend(line1 + line2, label1 + label2)
axes1.legend().remove()


fig.set_size_inches(10, 16, forward=True)
plt.show()
