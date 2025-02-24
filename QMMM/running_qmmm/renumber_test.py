import sys,os,re

g96=sys.argv[1]
f = open(g96,'r')
f0 = f.readlines()
#number = re.findall("\d+",g96)[1]
start=0
temp=[]
correction=0
prevatom=0
for line in f0:
    if 'END' in line:
        start=0
    if(start==0):
        temp.append(line)
    if(start==1):
        col0=line.split()[0]
        col1=line.split()[1]
        col2=line.split()[2]
        col4=line.split()[4]
        col3=line.split()[3]
        col5=line.split()[5]
        col6=line.split()[6]
        if(correction!=0):
            col3=str(prevatom+1)
        if(col2=='LA'):
            correction=correction+1
            col3=str(prevatom+1)
        prevatom=int(col3)
        while(len(col0)<5):
            col0=' '+col0
        while(len(col1)<3):
            col1=col1+' '
        col1=' '+col1
        col2='   '+col2
        while((len(col2)+len(col3))<15):
            col3=' '+col3
        while(len(col4)<15):
            col4=' '+col4
        while(len(col5)<15):
            col5=' '+col5
        while(len(col6)<15):
            col6=' '+col6
        temp.append(col0+col1+col2+col3+col4+col5+col6+'\n')
    if 'POSITION' in line:
        start=1

text=open('qmmm_input_md.g96','w')

for line in temp:
    text.write(line)
text.close()

