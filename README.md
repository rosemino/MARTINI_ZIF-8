In this folder you can find samples of LAMMPS input scripts we used to our differently-purposed classical MD simulations to derive the results found in the publication of DOI XXX.
Below you can find a list linking the name of an input file to what it was used for within our work. All of the input files presented are for model I of MARTINI 3 for mapping C. In the input file you can find short comments on the functionality of specific commands (or set of commands).

structure.in : input script used to derive data for determining BDF, ADF, RDF data in the coarse grained level.

mechanical_eq.in : input script used to equilibrate the system in the thermodynamic state corresponding to (300K, 0.2 GPa). This simulation was used to gather equilibrium values of lattice parameters as well as get an initial microstate to run further simulations in deformed states to get data to estimate the elastic tensor (simulation corresponding to the input script mechanical_exx.in and mechanical_exy.in). Same philosophy was followed for the (300K, 0.0 GPa) simulation.

mechanical_exx.in : input script used to run the simulation in a random deformed state (particularly here the one corresponding to the deformation of 0.2% exx). Same philosophy was used for the other % deformations.

mechanical_exy.in : input script used to run the simulation in a random deformed state (particularly here the one corresponding to the deformation of 0.2% exy). Same philosophy was used for the other % deformations.
