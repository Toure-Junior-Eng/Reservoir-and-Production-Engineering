import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

#creat a IPR data set
# IPR= Inflow Performance Relationship

ipr = pd.DataFrame({'Pwf':[4000,3500,3000,2500,2000,1500,1000,500,14.7],
                    'Q': [0,1999,3094,3902,4512,4963,5275,5458,5519]})
ipr
#create a TPC data set
# TPC= Tubing Performance Curve
 
q = np.arange(1000,6500,500)

p_190 = [1334,1400,1487,1592,1712,1843,1984,2132,2287,2446,2609]

p_2375 = [1298,1320,1351,1390,1435,1487,1545,1609,1677,1749,1824]

p_2875 = [1286,1294,1305,1319,1336,1356,1378,1403,1431,1461,1493]

tpc = pd.DataFrame({'q':q, 'Pwf(1.90" tbg)':p_190, 'Pwf(2.375"tbg)': p_2375,'Pwf(2.875"tbg)':p_2875})
tpc   

# Plotting the Nodal Analysis of a Gas Well

# BHP= Bottom Hole Pressure 
# Q= Flow Rate of the Gas
plt.figure(figsize=(9,5))
plt.plot(ipr['Q'], ipr['Pwf'], label = 'IPR', lw=1.5)
plt.plot(tpc['q'],tpc['Pwf(1.90" tbg)'],label='TPC for 1.9" tubing', lw=1.5)
plt.plot(tpc['q'],tpc['Pwf(2.375"tbg)'],label='TPC for 2.375" tubing', lw=1.5)
plt.plot(tpc['q'],tpc['Pwf(2.875"tbg)'],label='TPC for 2.875" tubing', lw=1.5)
plt.xlabel('FlowRate Q(Mscf/D)')
plt.ylabel('Flowing BHP(Psia)')
plt.title('Nodal Analysis for a Gas Well')
plt.grid()
plt.legend()