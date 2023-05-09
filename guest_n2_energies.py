"""
Created on Sun Mar 12 19:13:59 2023

@author: Cecilia Alvares
"""

import numpy as np

# --------------------------------------------------------------------------------------------------------------------------
# This is just to read the log.lammps dat saved in the MD simulation and transforming it into a 50000x25 array in python
# File log.lammps.dat = log.lammps but with format .dat now.

columns = 25
lines = int(500000/10)

A=[]
flag = 0
check = 'Step c_2[1] c_2[2] c_4[1] c_4[2] c_6[1] c_6[2] c_8[1] c_8[2] c_10[1] c_10[2] c_12[1] c_12[2] c_14[1] c_14[2] c_16[1] c_16[2] c_18[1] c_18[2] c_20[1] c_20[2] c_22[1] c_22[2] c_24[1] c_24[2] \n'

ofi = open("log.lammps.dat", 'r')
while flag != 1:
    dump = ofi.readline()
    #print (dump)
    if dump == check:
        flag = 1
for it_1 in range(lines):
        dump = ofi.readline()
        #dump = dump[0:32]
        e = dump.split(' ')
        for it_2 in range (0, len(e)):
            if (e[it_2] == '') or (e[it_2] == '\n'):
                continue
            value = float(e[it_2])
            A = np.append(A,float(value))
A = np.array(A,float)
A = A.reshape(lines,columns)

average_values = np.zeros((1,25))
for it_1 in range (0, len(A)):
    for it_2 in range (0, 25):
        average_values[0,it_2] = average_values[0,it_2] + A[it_1,it_2]
        
average_values = average_values/lines

# Variables inte_XY below will give the sum of interaction energy of all existing atoms Y in my system which come
# from the interaction with each and all superatom X existing in my system.
inte_14 = average_values[0,11] - average_values[0,1] - average_values[0,7]
inte_15 = average_values[0,17] - average_values[0,1] - average_values[0,9]
inte_24 = average_values[0,13] - average_values[0,3] - average_values[0,7]
inte_25 = average_values[0,19] - average_values[0,3] - average_values[0,9]
inte_34 = average_values[0,15] - average_values[0,5] - average_values[0,7]
inte_35 = average_values[0,21] - average_values[0,5] - average_values[0,9]

# Interaction energy felt by all the N2 molecules that compose the system with respect to each and all superatoms of a given type.
inte_1n2 = inte_14 + inte_15
inte_2n2 = inte_24 + inte_25
inte_3n2 = inte_34 + inte_35

# Total enregy is also defined.
inte_total = inte_1n2 + inte_2n2 + inte_3n2

output = np.array([[inte_total, inte_1n2, inte_2n2, inte_3n2]])
ending = np.savetxt('energies.txt', (output))

# Further process and normalization of output values of the code is made afterwards by the authors in order to present the values in the paper.
