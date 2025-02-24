#!/bin/bash
#SBATCH -A standby --gpus-per-node=1 --ntasks=16 --nodes=1
#SBATCH -t 04:00:00
tag=$( tail -n 1 qm.log )
i = $(echo $tag | awk '{print $1;}')
source ~/.bashrc
"0" | gmx traj -f traj.trr  -s qmmm.tpr -oxt qmmm.g96 -b '$i' -e '$i' 
wait
grompp -f qmmm.mdp -maxwarn 10 -c qmmm.g96 -n index.ndx -p topol.top -o qmmm.tpr
wait
bash submit.sh
