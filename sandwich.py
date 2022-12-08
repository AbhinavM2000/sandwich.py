import os
import sys
from ase import Atoms

pathway = sys.argv[1]
dimer = sys.argv[2]
interm = sys.argv[3]


pathway = open(pathway, 'r')
dimer = open(dimer, 'r')
pathway = pathway.readlines()
dimer = dimer.readlines()
newfile = dimer[0].strip() + "-" + pathway[0].strip() + ".xyz"
newfile = open(newfile, 'w')
newfile.write(str(int(pathway[0]) + 2) + '\n')
newfile.write("Properties=species:S:1:pos:R:3 pbc=\"F F F\""+'\n')
for i in range(2, len(dimer)):
    newfile.write(dimer[i].split()[0] + ' ' + dimer[i].split()[1] + ' ' + dimer[i].split()[2] + ' ' + dimer[i].split()[3] + '\n')
intermediate = {'ch2o': [-0.052, -8.059, -3.52],'ch2oh':[-15.03,-9.57,-15.47],'ch3o':[-14.247,-8.527,-18.056],'ch3oh':[-14.238,-8.411,-18.119],'cho':[1.119,-8.563,-3.231],'choh':[-15.43,-9.187,-16.23],'cooh':[-14.492,-8.662,-15.969],'h2coo':[-15.02,-5.358,-17.047],'h2cooh':[-15.238,-6.156,-16.672],'hcoo':[1.59,-8.398,-2.756],'hcooh1':[1.375,-8.59,-3.291]}
values1 = [float(intermediate[interm][0]), float(intermediate[interm][1]), float(intermediate[interm][2])]
for i in range(2, len(pathway)):
    pathway[i] = pathway[i].split()
    pathway[i][1] = float(pathway[i][1])
    pathway[i][2] = float(pathway[i][2])
    pathway[i][3] = float(pathway[i][3])
    pathway[i][1] = pathway[i][1] + values1[0]
    pathway[i][2] = pathway[i][2] + values1[1]
    pathway[i][3] = pathway[i][3] + values1[2]
    newfile.write(pathway[i][0] + ' ' + str(pathway[i][1]) + ' ' + str(pathway[i][2]) + ' ' + str(pathway[i][3]) + '\n')
newfile.close()
newfile = open(newfile.name, 'r')
newfile = newfile.readlines()
newfile1 = dimer[2][0] + dimer[2][1]+ dimer[3][0]+dimer[3][1]+"-" + interm + ".xyz"
newfile1 = open(newfile1, 'w')
for i in range(len(newfile)):
    newfile1.write(newfile[i])
newfile1.close()

os.system("ase gui " + newfile1.name + " -o " + (newfile1.name+ ".com"))
#open the newfile with ase gui
os.system("ase gui " + newfile1.name)
newfile8 = open(newfile1.name + ".com", 'r')
newfile8 = newfile8.readlines()
newfile9 = open(newfile1.name + ".com", 'w')
newfile9.write("#p opt=calcall freq b3lyp/genecp scf=maxcycles=200 pop=(nbo,savenbo,full,hirshfeld) gfinput" + '\n')
for i in range(len(newfile8)):
    newfile9.write(newfile8[i])
newfile9.close()
newfile6 = open(newfile1.name + ".com", 'r')
newfile6 = newfile6.readlines()
newfile7 = open(newfile1.name + ".com", 'w')
newfile7.write("%mem=20GB" + '\n')
for i in range(len(newfile6)):
    newfile7.write(newfile6[i])
newfile7.close()
newfile4 = open(newfile1.name + ".com", 'r')
newfile4 = newfile4.readlines()
newfile5 = open(newfile1.name + ".com", 'w')
newfile5.write("%nprocshared=20" + '\n')
for i in range(len(newfile4)):
    newfile5.write(newfile4[i])
newfile5.close()
newfile2 = open(newfile1.name + ".com", 'r')
newfile2 = newfile2.readlines()
newfile3 = open(newfile1.name + ".com", 'w')
newfile3.write("%chk="+newfile1.name+".chk" + '\n')
for i in range(len(newfile2)):
    newfile3.write(newfile2[i])
newfile3.close()
newfile10 = open(newfile1.name + ".com", 'r')
newfile10 = newfile10.readlines()
newfile11 = open(newfile1.name + ".com", 'w')
for i in range(len(newfile10)):
    if i != 4:
        newfile11.write(newfile10[i])
newfile11.close()
newfile12 = open(newfile1.name + ".com", 'r')
newfile12 = newfile12.readlines()
newfile13 = open(newfile1.name + ".com", 'w')
for i in range(len(newfile12)):
    newfile13.write(newfile12[i].replace('ASE', 'https://github.com/AbhinavM2000/sandwich.py'))
newfile13.close()

