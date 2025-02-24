#!/bin/sh
source ~/.bashrc
module load ngc/default
module load gromacs/2021.3.lvs
# Run make_ndx command
gmx make_ndx -f pdb2gmx.gro -o original_HOH.ndx <<-EOF
13
name 17 HOH
q
EOF

echo "Index file 'original_HOH.ndx' created successfully."
