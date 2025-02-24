#!/bin/sh
source ~/.bashrc
module load ngc/default
module load gromacs/2021.3.lvs
gmx make_ndx -f em.gro -o index.ndx << EOF
1|16
q
EOF
