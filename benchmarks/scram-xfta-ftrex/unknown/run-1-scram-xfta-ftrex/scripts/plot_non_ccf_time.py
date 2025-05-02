import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_csv('Tables-Final_wall.csv')

FaultTree = ["100-01", "100-02", "100-03", "100-04", "100-05", "100-06", "100-07", "100-08", "100-09", "200-01","200-02","200-03", "200-04", "200-05", "200-06", "200-07","200-08", "200-09", "500-01", "500-02", "500-03", "500-04"]
fig, ax = plt.subplots(figsize=(15, 7))
Numba = table.loc[:,'#'].values
new = table.loc[:,'XFTA'].values
SAPHSOLVE = table.loc[:,'SAPHSOLVE'].values
ScramB = table.loc[:,'SCRAM-BDD'].values
ScramM = table.loc[:,'SCRAM-MOCUS'].values
ScramR = table.loc[:,'SCRAM-ZBDD'].values
FTREXIDBDD = table.loc[:,'FTREX-ID-BDD'].values
FTREXIDZBDD = table.loc[:,'FTREX-ID-ZBDD'].values
FTREXNAMEBDD = table.loc[:,'FTREX-NAME-BDD'].values
FTREXNAMEZBDD = table.loc[:,'FTREX-NAME-ZBDD'].values


plt.scatter(np.arange(len(FaultTree)), new, label='XFTA', marker='x', c='red', s=180)
plt.scatter(np.arange(len(FaultTree)), SAPHSOLVE, label='SAPHSOLVE', marker='*', c='black', s=180)
plt.scatter(np.arange(len(FaultTree)), ScramB, label='SCRAM - BDD', marker='s', c='green', s=180)
plt.scatter(np.arange(len(FaultTree)), ScramM, label='SCRAM - MOCUS', marker='.', c='blue', s=250)
plt.scatter(np.arange(len(FaultTree)), ScramR, label='SCRAM - ZBDD', marker='v', c='magenta', s=180)
plt.scatter(np.arange(len(FaultTree)),FTREXIDBDD, label='FTREX-ID-BDD', marker='*', c='black', s=180)
plt.scatter(np.arange(len(FaultTree)), FTREXIDZBDD, label='FTREX-ID-ZBDD', marker='s', c='green', s=180)
plt.scatter(np.arange(len(FaultTree)), FTREXNAMEBDD , label='FTREX-NAME-BDD ', marker='.', c='blue', s=250)
plt.scatter(np.arange(len(FaultTree)), FTREXNAMEZBDD, label='FTREX-NAME-ZBDD', marker='v', c='magenta', s=180)


ax = plt.gca()
ax.set_xticks(np.arange(len(FaultTree)))  # set tick locations
ax.set_xticklabels(FaultTree, rotation=70)  # set tick labels
plt.xlabel('Input models', fontsize=26, weight='bold')
plt.ylabel('CPU Time [sec]', fontsize=26, weight='bold')
plt.yticks(np.arange(0, 9, 2))
plt.xticks(fontsize=26)
plt.yticks(fontsize=26)

plt.legend(fontsize=22, loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('Time-non-ccf.png', dpi=400, bbox_inches='tight')

plt.show()
