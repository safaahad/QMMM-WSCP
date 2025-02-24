SOLat=3
SOLmol=$(grep SOL 3_added_la_md_*.g96 | wc -l)
QSLmol=$(grep QSL 3_added_la_md_*.g96 | wc -l)
ans=$((SOLmol/SOLat))
qsl=$((QSLmol/SOLat))
sed -i -e "s/QSL .*/QSL $qsl/g" topol.top
sed -i -e "s/SOL .*/SOL $ans/g" topol.top
sed "s/ 1712 CLA/ 1712 CAQ/g" 3_added_la_md_*.g96 > 3_new_added_la_md.g96
