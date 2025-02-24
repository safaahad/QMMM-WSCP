import sys,math,re

g96_file=sys.argv[1]
with open(g96_file,'r') as g96:
    reflines = g96.readlines()
    number = re.findall("\d+",g96_file)[1]
lineN    = 0
for obj in reflines:
    line  = obj.strip()
    lineN += 1
    if 'POSITION' in line:
        xyz1 = lineN
    elif 'BOX' in line:
        xyz2 = lineN-1
        break
    else:
        continue

lineN       = 0
st1,st3     = '',''
pd1,pd2,pd3 = [],[],[]
for obj in reflines:
    #print(obj)
    line  = obj.strip()
    #print(line)
    lineN += 1
    if lineN <= xyz1:
        st1 += obj
    elif lineN >= xyz2:
        st3 += obj
    else:
        if len(line.split()) > 3 :
            if line.split()[1] == 'SOL':
                pd2.append(line)
            elif line.split()[1] == 'NA':
                pd3.append(obj)
            else:
                pd1.append(obj)
                if line.split()[1] == 'CLA':
                    if int(line.split()[0]) == 1712:
                        if line.split()[2] == 'OBD':
                            x1,y1,z1 = float(line.split()[4]),float(line.split()[5]),float(line.split()[6])
                            qx,qy,qz = float(line.split()[4]),float(line.split()[5]),float(line.split()[6])
                        else:
                            continue
                    elif int(line.split()[0]) == 1711:
                        if line.split()[2] == 'OBD':
                            x2,y2,z2 = float(line.split()[4]),float(line.split()[5]),float(line.split()[6])
                        else:
                            continue
                    else:
                        continue
temp1,temp2 = [],[]
for i in range(0,len(pd2),3):
    wx,wy,wz = float(pd2[i].split()[4]),float(pd2[i].split()[5]),float(pd2[i].split()[6])
    dx,dy,dz = 10.0*(x1-wx),10.0*(y1-wy),10.0*(z1-wz)
    r2       = dx**2+dy**2+dz**2
    temp1.append(r2)
for i in range(0,len(pd2),3):
    wx,wy,wz = float(pd2[i].split()[4]),float(pd2[i].split()[5]),float(pd2[i].split()[6])
    dx,dy,dz = 10.0*(x2-wx),10.0*(y2-wy),10.0*(z2-wz)
    r2       = dx**2+dy**2+dz**2
    temp2.append(r2)


i1 = temp1.index(min(temp1))*3
i2 = temp1.index(sorted(temp1)[1])*3

#i2 = temp2.index(min(temp2))*3
correct = []
correct.append(pd2[i1])
correct.append(pd2[i1+1])
correct.append(pd2[i1+2])
correct.append(pd2[i2])
correct.append(pd2[i2+1])
correct.append(pd2[i2+2])

#exit()

for i in range(len(pd2)):
    if pd2[i] in correct:
        continue
    else:
        correct.append(pd2[i])

if len(correct) != len(pd2):
    print('line number diff')
    exit()

print("HERE")
resn,atmn = int(pd1[-1].strip().split()[0])+1,int(pd1[-1].strip().split()[3])+1
nd2       = []
for i in range(len(correct)):
    if resn == 1713:
        mol = 'QSL'
        if correct[i].split()[2] == 'OW':
            atm = 'OQ'
        elif correct[i].split()[2] == 'HW1':
            atm = 'HQ1'
        elif correct[i].split()[2] == 'HW2':
            atm = 'HQ2'
        else:
            print('not available atom name')
            print(correct[i])
            exit()

    else:
        mol = correct[i].split()[1]
        atm = correct[i].split()[2]

    x1 = '{:{align}{width}}'.format('%d'%resn,align='>',width=5)
    x2 = '{:{align}{width}}'.format('%s'%mol,align='>',width=4)
    x3 = '{:{align}{width}}'.format('%s'%atm,align='>',width=6)
    x4 = '{:{align}{width}}'.format('%d'%atmn,align='>',width=9)
    x5 = '{:{align}{width}}'.format('%.9f'%float(correct[i].split()[4]),align='>',width=15)
    x6 = '{:{align}{width}}'.format('%.9f'%float(correct[i].split()[5]),align='>',width=15)
    x7 = '{:{align}{width}}'.format('%.9f'%float(correct[i].split()[6]),align='>',width=15)
    nd2.append(x1+x2+x3+x4+x5+x6+x7+'\n')
    atmn += 1
    if i % 3 == 2:
        resn += 1

nx,ny,nz = float(nd2[0].strip().split()[4]),float(nd2[0].strip().split()[5]),float(nd2[0].strip().split()[6])
dx,dy,dz = 10.0*(qx-nx),10.0*(qy-ny),10.0*(qz-nz)
print('distance b/w 1702 and closest water',math.sqrt(sorted(temp1)[0]))
print('distance b/w 1702 and next closest water',math.sqrt(sorted(temp1)[1]))


wrt = pd1+nd2+pd3

for i in range(len(wrt)):
    st1 += wrt[i]
st1 += st3

with open('2_find_q_waters_md_'+number+'.g96','w') as ofile:
    ofile.write(st1)


