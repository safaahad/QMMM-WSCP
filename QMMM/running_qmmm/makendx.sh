#!/bin/sh
source ~/.bashrc
module load ngc/default
module load gromacs/2021.3.lvs -gpu
gmx make_ndx -f qmmm_input_md.g96 -o index.ndx << EOF
1|13|14|15
name 28 Solute
0&!28
name 29 Solvent
13|15|16|a 6141-6151| a 8803-8813
name 30 QM_atoms
0&!30
name 31 MM_atoms
q
EOF
