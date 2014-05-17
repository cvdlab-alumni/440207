from larcc import *

def diagram2cell(diagram,master,cell):
   mat = diagram2cellMatrix(diagram)(master,cell)
   diagram =larApply(mat)(diagram)  
   
   """
   # yet to finish coding
   V, CV1, CV2, n12 = vertexSieve(master,diagram)
   masterBoundaryFaces = boundaryOfChain(CV,FV)([cell])
   diagramBoundaryFaces = lar2boundaryFaces(CV,FV)
   """
   
   #codice omesso
   #V = master[0] + diagram[0]
   #offset = len(master[0])
   
   V,CV = master
   CV = [c for k,c in enumerate(master[1]) if k != cell]
   #prendo le celle da vertexSieve (libreria boolean.py)
   V, CV1, CV2, n12 = vertexSieve(master,diagram)
   #CV sarà la somma delle celle di CV1 e CV2
   CV = CV1+CV2
   master = V, CV
   return master
