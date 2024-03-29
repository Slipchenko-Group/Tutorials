# Ligand Parameterization

This tutorial walks users through the process of preparing GAFF2 parameters for ligands. The users are expected to have access to a supercomputer and depot.


## Prepare PDB file 

1. Extract the ligand structure from the protein-ligand complex of interest.

2. Protonate the ligand structure based on the desired pH.

3. Conduct energy minimization on the protonated structure.

4. Save the minimized structure in PDB format and modify it to adhere to the format of the file `1m.pdb`, ensuring the right spacing between columns.

Steps 2 and 3 can be done in Avogadro or IQmol.

## Assign atomtypes and charges with antechamber

1. Load amber.

   ```
   module load amber
   ```

2. Use antechamber specifying the GAFF2 force field (-at gaff2), the AM1-BCC2 charge method (-c bcc), the net charge of the molecule (-nc 0), and generate a mol2-type file (-fo mol2).


   ```
   antechamber -i 1m.pdb -fi pdb -o 1m.mol2 -fo mol2 -c bcc -nc 0 -at gaff2
   ```

3. Open the `sqm.out` file and verify that the calculation was completed succesfully. Remove all intermediate files except for the mol2 file, which contains the ligand coordinates along with atom types and atomic charges. 


## Find missing force field parameters with parmchk2

1. Use parmchk2 to generate a parameter file named `1m.frcmod` that includes missing parameters.

   ```
   parmchk2 -i 1m.mol2 -f mol2 -o 1m.frcmod -s gaff2
   ```

2. Examine the parameter file to find placeholders (filled with zeros) with the comment "ATTN: needs revision." In such instances, you will need to parameterize it manually. Additionally, inspect the penalty scores associated with the parameters. High penalty scores indicate parameters that may require further optimization. 

## Create amber topologies using tleap

1. Run tleap using the supplied input file `leap.in`. Before execution, adjust this input file to align with system specifications. 

   ```
   tleap -f leap.in
   ```
## Convert amber topologies to gromacs topologies using parmed

1. Load parmed. 

   ```
   source /depot/lslipche/apps/parmed/parmed.env
   ```

2. Run parmed using the provided python script `parmed_gromacs.py`. Before execution, customize the script to match your system specifications.

   ```
   python parmed_gromacs.py
   ```

## Further Reading

1. [Antechamber](https://ambermd.org/antechamber/ac.html)
2. [ParmEd](https://parmed.github.io/ParmEd/html/index.html#)
3. [Overview of AmberTools20](https://docs.bioexcel.eu/2020_06_09_online_ambertools4cp2k/01-overview/index.html)