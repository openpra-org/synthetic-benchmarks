import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_csv('Tables-Final_wall.csv')

Numba = table.loc[:,'#'].values
new = table.loc[:,'Time-XFTA'].values
SAPHSOLVE = table.loc[:,'Time-SAPHSOLVE'].values
ScramB = table.loc[:,'Time-SCRAM-BDD'].values
ScramM = table.loc[:,'Time-SCRAM-MOCUS'].values
ScramR = table.loc[:,'Time-SCRAM-ZBDD'].values


fig, ax1 = plt.subplots()
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.scatter(np.arange(len(Numba)), new, label='XFTA', marker='.', c='red', s=150)
ax1.scatter(np.arange(len(Numba)), SAPHSOLVE, label='SAPHSOLVE', marker='.', c='black', s=150)
ax1.scatter(np.arange(len(Numba)), ScramB, label='SCRAM - BDD', marker='.', c='green', s=150)
ax1.scatter(np.arange(len(Numba)), ScramM, label='SCRAM - MOCUS', marker='.', c='blue', s=150)
ax1.scatter(np.arange(len(Numba)), ScramR, label='SCRAM - ZBDD', marker='.', c='magenta', s=150)

ax1.set_xticks(np.arange(len(Numba))-0.5)  # set tick locations
# ax1.set_xticklabels(Numba, rotation=0)  # set tick labels
ax1.set_xlabel('Input models', fontsize=12)
ax1.set_ylabel('CPU Time [sec]', fontsize=12)
ax1.set_yticks(np.arange(0, 1100, 100))
ax1.set_xticks(np.arange(0, 200, 20))
ax2 = ax1.twinx()
time_labels = ['Memory-XFTA', 'Memory-SAPHSOLVE', 'Memory-SCRAM-BDD', 'Memory-SCRAM-MOCUS', 'Memory-SCRAM-ZBDD']
Numba_m = table.loc[:,'#'].values
new_m = table.loc[:,'Memory-XFTA'].values
SAPHSOLVE_m = table.loc[:,'Memory-SAPHSOLVE'].values
ScramB_m = table.loc[:,'Memory-SCRAM-BDD'].values
ScramM_m = table.loc[:,'Memory-SCRAM-MOCUS'].values
ScramR_m = table.loc[:,'Memory-SCRAM-ZBDD'].values
ax2.scatter(np.arange(len(Numba_m)), new_m, marker='v', c='red', s=80)
ax2.scatter(np.arange(len(Numba_m)), SAPHSOLVE_m, marker='v', c='black', s=80)
ax2.scatter(np.arange(len(Numba_m)), ScramB_m, marker='v', c='green', s=80)
ax2.scatter(np.arange(len(Numba_m)), ScramM_m, marker='v', c='blue', s=80)
ax2.scatter(np.arange(len(Numba_m)), ScramR_m, marker='v', c='magenta', s=80)

ax2.set_ylabel('Memory [MB]', fontsize=12)
ax2.set_yticks(np.arange(0, 19000, 2000))
ax2.set_xticks(np.arange(0, 200, 20))

ax1.legend(fontsize=10, loc='upper left')
ax2.legend(fontsize=10, loc='upper right')
ax1.grid()
plt.tight_layout()
plt.savefig('Memory-Time.png', dpi=400, bbox_inches='tight')

plt.show()
