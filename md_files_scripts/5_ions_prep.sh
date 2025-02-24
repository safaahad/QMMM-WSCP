#!/bin/bash
source ~/.bashrc
module load ngc/default
module load gromacs/2021.3.lvs
# Define file names
topol_file="topol.top"
index_file="index_sol.ndx"

# Backup the original topol.top
cp "$topol_file" "$topol_file.backup"

# Change the last solvent molecules' name from "SOL" to "newSOL"
sed -i '/CLA/{n;s/SOL/newSOL/;}' topol.top
# Run genion with the updated files
gmx genion -s ions.tpr -o solv_ions.gro -p "$topol_file" -n "$index_file" -pname NA -nname CL -neutral<<EOF
18
EOF
# Switch back "newSOL" to "SOL" in the topol.top (restoring the backup)
sed -i '/CLA/{n;s/newSOL/SOL/;}' topol.top
