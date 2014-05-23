# This Python file uses the following encoding: utf-8

from pyplasm import *
from larcc import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

def trasparenza(oggetto):
    return MATERIAL([1,1,1,0.1, 0,0,0.8,0.5, 1,1,1,0.1, 1,1,1,0.1, 100])(oggetto)

#casa torresina
master = assemblyDiagramInit([11,11,2])([[.3,1,.1,3,.1,3,.1,1,.1,4,.3],[.3,1.5,.1,1.5,.1,1,.1,3,.1,3,.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))

#in rosso i numeri delle celle
casa = cellNumbering (master,hpc)(range(len(CV)),RED,1)
VIEW(casa)

#RIMOZIONE CELLE
#stanze
roomsToRemove = [25,29,33,37,41,
                 69,73,77,81,85,
                 113,117,121,125,129,
                 157,161,165,169,173,
                 201,205,209,213,217]
#pareti
wallsToRemove = [3,7,23,27,35,39,55,59,63,71,75,79,83,131,151,175,195,219,239,
                 191,211,143,163,135,203]
#colonne
columnsToRemove = [1,5,57,61,153,197]
#pavimenti
floorsToRemove = [130,152,174,196,218,128,216,150,172,194,238,240]

toRemove = roomsToRemove + wallsToRemove + columnsToRemove + floorsToRemove


#in CV di master inserisco solo le celle NON da rimuovere
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
VIEW(hpc)


#CREAZIONE PORTE E FINESTRE NELLE PARETI
#porta d'entrata (cella 38)
diagram = assemblyDiagramInit([1,2,2])([[.3],[1,.5],[2.2,.5]])
master = diagram2cell(diagram,master,38)
#porta soggiorno/giardino (cella 79)
diagram = assemblyDiagramInit([1,3,2])([[.3],[1,1,1],[2.2,.5]])
master = diagram2cell(diagram,master,79)
#porta camera1/giardino (cella 94)
diagram = assemblyDiagramInit([3,1,2])([[1,1,1],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,94)
#porta camera2/giardino (cella 151)
diagram = assemblyDiagramInit([3,1,2])([[1,1,2],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,151)
#porta soggiorno/corridoio (cella 71)
diagram = assemblyDiagramInit([1,3,2])([[.3],[.25,.5,.25],[2.2,.5]])
master = diagram2cell(diagram,master,71)
#porta corridoio/camera1 (cella 90)
diagram = assemblyDiagramInit([3,1,2])([[1.25,.5,1.25],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,90)
#porta corridoio/bagno1 (cella 87)
diagram = assemblyDiagramInit([3,1,2])([[1.25,.5,1.25],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,87)
#porta corridoio/camera2 (cella 116)
diagram = assemblyDiagramInit([3,1,2])([[.25,.5,.25],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,116)
#porta corridoio/camera3 (cella 126)
diagram = assemblyDiagramInit([1,3,2])([[.3],[.5,.5,.5],[2.2,.5]])
master = diagram2cell(diagram,master,126)
#porta camera3/bagno2 (cella 122)
diagram = assemblyDiagramInit([1,3,2])([[.3],[.5,.5,.5],[2.2,.5]])
master = diagram2cell(diagram,master,122)
#finestra soggiorno (cella 59)
diagram = assemblyDiagramInit([2,1,3])([[2,1],[.3],[1,1.4,.3]])
master = diagram2cell(diagram,master,59)
#finestra1 camera2 (cella 117)
diagram = assemblyDiagramInit([2,1,3])([[.5,.5],[.3],[1,1.4,.3]])
master = diagram2cell(diagram,master,117)
#finestra2 camera2 (cella 158)
diagram = assemblyDiagramInit([1,4,3])([[.3],[1,.5,1,.5],[1,1.4,.3]])
master = diagram2cell(diagram,master,158)
#finestra camera3 (cella 150)
diagram = assemblyDiagramInit([1,2,3])([[.3],[1,.5],[1,1.4,.3]])
master = diagram2cell(diagram,master,150)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
VIEW(hpc)

#RIMOZIONE PORTE E FINESTRE
porteToRemove = [160,166,172,178,184,190,196,202,208,214]
finestreToRemove = [219,228,231,237,243]
doors =  master[0], [cell for k,cell in enumerate(master[1]) if (k in porteToRemove)]
windows = master[0], [cell for k,cell in enumerate(master[1]) if (k in finestreToRemove)]

porte = COLOR([100/255.,70/255.,0/255.])(STRUCT(MKPOLS(doors)))
finestre = trasparenza(STRUCT(MKPOLS(windows)))

toRemove = [160,219,166,178,184,190,196,202,208,214,172,228,237,231,243]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

mura = STRUCT(MKPOLS(master))

floor0 = STRUCT([mura,porte,finestre])
VIEW(floor0)

