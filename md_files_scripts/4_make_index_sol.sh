#!/bin/sh
source ~/.bashrc
module load ngc/default
module load gromacs/2021.3.lvs
gmx make_ndx -f solv.gro -o index_sol.ndx -n solvated<< EOF
13&!17
name 18 newSOL
q
EOF
