from pyplasm import *
from larcc import *
DRAW = COMP([VIEW,STRUCT,MKPOLS])

#funzione che, avendo come parametri il master, una suddivisione di una cella e
#il numero della cella, restituisce il master privo della porta passata come intervallo

def easy_mer_num_del(master,blocchi,intervalli,cella):
    #variabili varie
    V,CV = master
    x,y,z = blocchi
    intX,intY,intZ = intervalli
    #creazione porta nella cella
    toMerge = cella
    diagram= assemblyDiagramInit(blocchi)(intervalli)
    master = diagram2cell(diagram,master,toMerge)    
    #rimozione porta
    toRemove = [len(CV)-1+len(intZ)]
    master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
    return master


#in quest'altra versione non si passa la cella come parametro ma la si sceglie dopo aver visto
#l'enumerazione dei blocchi, allo stesso modo si sceglie quali blocchi eliminare
def easy_mer_num_del_2(master,blocchi,intervalli):
    #variabili varie
    V,CV = master
    x,y,z = blocchi
    intX,intY,intZ = intervalli
    #creazione porta nella cella (vengono mostrati i blocchi tra cui scegliere)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),ORANGE,1)
    VIEW(hpc)
    toMerge = input()
    diagram= assemblyDiagramInit(blocchi)(intervalli)
    master = diagram2cell(diagram,master,toMerge)    
    #rimozione porta (vengono mostrati i blocchi tra cui scegliere)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),ORANGE,1)
    VIEW(hpc)
    toRemove = []
    choice = input()
    while(choice != -1):
        toRemove.append(choice)
        choice = input()
    master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
    return master


#TEST
#creo un master e una suddivisione di una porta
m = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
b = [3,1,2]
i =[[2,1,2],[.3],[2.2,.5]]
c = 29
#rimuovo i locali interni (per poter visualizzare meglio il risultato)
toRemove = [13,33,17,37]
V,CV = m
m = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#visualizzo la numerazione delle celle prima di entrare nella funzione 'easy_mer_num_del'
hpc = SKEL_1(STRUCT(MKPOLS(m)))
hpc = cellNumbering (m,hpc)(range(len(m[1])),ORANGE,2)
VIEW(hpc)

#assegno a 'new' il nuovo master..
new = easy_mer_num_del(m,b,i,c)
#re-visualizzo la numerazione delle celle dopo la funzione 'easy_mer_num_del'
hpc = SKEL_1(STRUCT(MKPOLS(new)))
hpc = cellNumbering (new,hpc)(range(len(new[1])),ORANGE,2)
VIEW(hpc)
#..e lo disegno
DRAW(new)

new2 = easy_mer_num_del_2(m,b,i)
#re-visualizzo la numerazione delle celle dopo la funzione 'easy_mer_num_del_2'
hpc2 = SKEL_1(STRUCT(MKPOLS(new2)))
hpc2 = cellNumbering (new2,hpc2)(range(len(new2[1])),ORANGE,2)
VIEW(hpc2)
#..e lo disegno
DRAW(new2)


