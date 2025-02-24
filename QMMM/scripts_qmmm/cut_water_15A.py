import sys,math
import re
import random

def cut_water_outside_15A(mw,x1,y1,z1,x2,y2,z2):
        temp1 = list()
        for i in range(len(x1)):
                temp2 = list()
                for j in range(len(x2)):
                        dx = (x1[i]-x2[j])*10.0
                        dy = (y1[i]-y2[j])*10.0
                        dz = (z1[i]-z2[j])*10.0
                        r  = pow(dx,2)+pow(dy,2)+pow(dz,2)
                        temp2.append(r)
                temp1.append(temp2)

        temp3,temp4 = list(),list()
        for i in range(len(temp1)):
                if min(temp1[i]) <= 225.0:
                        temp3.append(mw[i*3])
                        temp3.append(mw[i*3+1])
                        temp3.append(mw[i*3+2])
                elif min(temp1[i]) > 225.0 and min(temp1[i]) <= 230.0:
                        temp4.append(mw[i*3])
                        temp4.append(mw[i*3+1])
                        temp4.append(mw[i*3+2])
        return temp3,temp4

def formating(line):
        string = ''
        for i in range(len(line)):
                line1 = line[i].strip().split()
                x0 = '{:{align}{width}}'.format('%s'%str(line1[0]),align='>',width=5)
                x1 = '{:{align}{width}}'.format('%s'%str(line1[1]),align='>',width=4)
                x2 = '{:{align}{width}}'.format('%s'%str(line1[2]),align='>',width=6) 
                x3 = '{:{align}{width}}'.format('%s'%str(line1[3]),align='>',width=9)
                x4 = '{:{align}{width}}'.format('%.9f'%float(line1[4]),align='>',width=15)
                x5 = '{:{align}{width}}'.format('%.9f'%float(line1[5]),align='>',width=15)
                x6 = '{:{align}{width}}'.format('%.9f'%float(line1[6]),align='>',width=15)
                string += x0+x1+x2+x3+x4+x5+x6+'\n'
        return string

def move_cl(string,x,y,z):
        x0 = '{:{align}{width}}'.format('%s'%str(string.split()[0]),align='<',width=5)
        x1 = ' NA'
        x2 = '    NA'
        x3 = '{:{align}{width}}'.format('%s'%str(string.split()[3]).strip(),align='>',width=10)
        x4 = '{:{align}{width}}'.format('%.9f'%float(x),align='>',width=15)
        x5 = '{:{align}{width}}'.format('%.9f'%float(y),align='>',width=15)
        x6 = '{:{align}{width}}'.format('%.9f'%float(z),align='>',width=15)
        return x0+x1+x2+x3+x4+x5+x6

def move_ions_to_box(cut_wat2,cl):
        temp1,temp2 = list(),list()
        rand = random.sample(range(0,len(cut_wat2),3),len(cl))

        lineN = 0
        for i in range(len(cut_wat2)):
                if i in rand:
                        temp2.append(move_cl(cl[lineN],cut_wat2[i].split()[4],cut_wat2[i].split()[5],cut_wat2[i].split()[6]))
                elif i-1 in rand:
                        continue
                elif i-2 in rand:
                        continue
                else:
                        temp1.append(cut_wat2[i])

        return temp1,temp2

def main(inputfile1):
        ifile = open(inputfile1,'r')
        outputfile = '1_cut_waters_'+inputfile1
        ofile = open(outputfile,'w')
        reflines = ifile.readlines()

        lineN = 0
        for obj in reflines:
                line  = obj.strip()
                lineN += 1
                if 'POSITION' in line:
                        xyz1 = lineN
                elif 'VELOCITY' in line:
                        xyz2 = lineN-1
                elif 'BOX' in line:
                        size = lineN-1
                else:
                        continue

        string1,string2,string3 = '','',''
        lineN                   = 0
        x1,y1,z1                = list(),list(),list()
        x2,y2,z2                = list(),list(),list()
        qw,cl,pt                = list(),list(),list()
        mw                      = list()
        for obj in reflines:
                line  = obj.strip()
                lineN += 1
                if lineN <= xyz1:
                        string1 += obj
                elif lineN >= size:
                        string3 += obj
                else:
                        if lineN > xyz1:
                                if line.split()[1] == 'SOL':
                                        mw.append(line)
                                        if line.split()[2] == 'OW':
                                                x1.append(float(line.split()[4]))
                                                y1.append(float(line.split()[5]))
                                                z1.append(float(line.split()[6]))
                                        else:
                                                continue
                                elif line.split()[1] == 'NA':
                                        cl.append(line)
                                else:
                                        pt.append(obj)
                                        if line.split()[2][0:1] != 'H':
                                                x2.append(float(line.split()[4]))
                                                y2.append(float(line.split()[5]))
                                                z2.append(float(line.split()[6]))
                        else:
                                continue
 
        cut_wat1,cut_wat2 = cut_water_outside_15A(mw,x1,y1,z1,x2,y2,z2)
        cut_wat2,cl       = move_ions_to_box(cut_wat2,cl)
        string2           = formating(cut_wat1+cut_wat2+cl)
        print(inputfile1)
        ofile.write(string1)
        for i in range(len(pt)):
                ofile.write(pt[i])
        ofile.write(string2)
        ofile.write(string3)
main(sys.argv[1])
