In this folder you can find samples of LAMMPS input scripts we used to our differently-purposed classical MD simulations to derive the results found in the publication of DOI XXX.
Below you can find a list linking the name of an input file to what it was used for within our work. All of the input files presented are for model I of MARTINI 3 for mapping C. In the input file you can find short comments on the functionality of specific commands (or set of commands).

structure.in : input script used to derive data for determining BDF, ADF, RDF data in the coarse grained level.

mechanical_eq.in : input script used to equilibrate the system in the thermodynamic state corresponding to (300K, 0.2 GPa). This simulation was used to gather equilibrium values of lattice parameters as well as get an initial microstate to run further simulations in deformed states to get data to estimate the elastic tensor (simulation corresponding to the input script mechanical_exx.in and mechanical_exy.in). Same philosophy was followed for the (300K, 0.0 GPa) simulation.

mechanical_exx.in : input script used to run the simulation in a random deformed state (particularly here the one corresponding to the deformation of 0.2% exx). Same philosophy was used for the other % deformations.

mechanical_exy.in : input script used to run the simulation in a random deformed state (particularly here the one corresponding to the deformation of 0.2% exy). Same philosophy was used for the other % deformations.

amorphization.in : input script used to run a 200ns long simulation for the sake of evaluating if the model reproduces the amorphization.

thermal_expa.in : input script used to run the simulation at 1 atm and 272.5K and get the resulting equilibrium volume once the system has equilibrated. The same philosophy is used for the 300K temperature to then estimate the volume expansion coefficient.

guest_n2.in : input script used to run the simulation of ZIF-8 with 51 N2 molecules at the corresponding pressure and temperature. Same philosophy was used for MeOH.

guest_n2_energies.in : input script used to assess the LJ interaction between superatoms of the MOF and N2 molecules. The philosophy of this script is the same as the one in the guest_n2.in script and in fact, only one simulation could have been run for everything. I ran separately because ideas did not come in order. This simulation uses the equilibrated_pos.dat script coming from the guest_n2.in simulation of the respective model. A post processing python code was used to ultimately get data with the meaning given in the official publication. Such python code is also presented here for what is worth (see guest_n2_energies.py).

