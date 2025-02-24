#!/bin/sh
source ~/.bashrc
module load ngc/default
module load gromacs/2021.3.lvs
gmx make_ndx -f solv.gro -o solvated.ndx << EOF
q
EOF
