# This Python file uses the following encoding: utf-8

from pyplasm import *
from larcc import *

from exercise1 import *

GRID = COMP([INSR(PROD),AA(QUOTE)])

#giardino
controlpoints = [[0,3.3],[4.25,-3],[4.25,6.6],[8,3.3],[8.4,0]]
dom = larDomain([64])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
garden = STRUCT(MKPOLS(obj))
garden = STRUCT([garden,POLYLINE([[0,3.3],[0,0],[8.4,0]])])
garden3D = DIFFERENCE([PROD([SOLIDIFY(garden),Q(0.3)]),CUBOID([8.4,.1,.3])])

#recinto
controlpoints = [[.01,3.4],[4.26,-2.9],[4.26,6.7],[8.01,3.4],[8.51,.1]]
dom = larDomain([64])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
fence = STRUCT(MKPOLS(obj))
fence = STRUCT([fence,POLYLINE([[.01,3.4],[0,0],[8.51,.1]])])
fence3D = PROD([SOLIDIFY(fence),Q(1)])
fence3D = DIFFERENCE([fence3D,PROD([SOLIDIFY(garden),Q(1)])])
garden3D = COLOR([0.012,0.753,0.234])(garden3D)

out = T([1,2])([4.5,7.6])(STRUCT([garden3D,fence3D]))

VIEW(STRUCT([floor0,out]))

#ALTRI PIANI

master1 = assemblyDiagramInit([11,11,2])([[.3,1,.1,3,.1,3,.1,1,.1,4,.3],[.3,1.5,.1,1.5,.1,1,.1,3,.1,3,.3],[.3,2.7]])

#finestra soggiorno (cella 87)
diagram1 = assemblyDiagramInit([2,1,3])([[2,1],[.3],[1,1.4,.3]])
master1 = diagram2cell(diagram1,master1,87)
#finestra camera nuova (cella 130)
diagram1 = assemblyDiagramInit([2,1,3])([[.5,.5],[.3],[1,1.4,.3]])
master1 = diagram2cell(diagram1,master1,130)
#finestra camera2 (cella 233)
diagram1 = assemblyDiagramInit([1,4,3])([[.3],[1,.5,1,.5],[1,1.4,.3]])
master1 = diagram2cell(diagram1,master1,233)
#finestra camera3 (cella 225)
diagram1 = assemblyDiagramInit([1,2,3])([[.3],[1,.5],[1,1.4,.3]])
master1 = diagram2cell(diagram1,master1,225)

V1,CV1 = master1
roomsToRemove1 = [25,29,33,37,41,
                  69,73,77,81,85,
                  112,116,120,124,128,
                  155,159,163,167,171,
                  199,203,207,211,215]
wallsToRemove1 = [3,7,23,27,35,39,55,59,63,71,75,79,83,149,193,189,209,141,161,133,201]
columnsToRemove1 = [1,5,57,61]
windowsToRemove1 = [239,248,257,251,263]

windows1 = V1,[cell for k,cell in enumerate(CV1) if (k in windowsToRemove1)]

toRemove1 = roomsToRemove1 + wallsToRemove1 + columnsToRemove1 + windowsToRemove1
master1 = V1,[cell for k,cell in enumerate(CV1) if not (k in toRemove1)]

#porta d'entrata (cella 38)
diagram1 = assemblyDiagramInit([1,2,2])([[.3],[1,.5],[2.2,.5]])
master1 = diagram2cell(diagram1,master1,38)

V1,CV2 = master1
toRemove2 = [212]
door1 = V1,[cell for k,cell in enumerate(CV2) if (k in toRemove2)]
master1 = V1,[cell for k,cell in enumerate(CV2) if not (k in toRemove2)]

finestre1 =trasparenza(STRUCT(MKPOLS(windows1)))
porta1 = COLOR([100/255.,70/255.,0/255.])(STRUCT(MKPOLS(door1)))

#pianerottolo
muro_di_fondo = T([1,2,3])([-2,7,.3])(CUBOID([2,-.3,2.7]))
stair2D = SOLIDIFY(POLYLINE([[0,-3],[-2,-3],[-2,-2],[-3,-2],[-3,0],[-2,0],[-2,7],[0,7],[0,-3]]))
stair3D = PROD([stair2D,Q(.3)])
stairTerra = PROD([SOLIDIFY(POLYLINE([[0,-2],[-3,-2],[-3,0],[-2,0],[-2,7],[0,7],[0,-2]])),Q(.3)])
rampaBase = PROD([SOLIDIFY(POLYLINE([[0,0],[.3,0],[0,1.5],[0,0]])),Q(2)])
rampaTerra = T([1,2])([-2,-2])(S(2)(-1)(MAP([S3,S2,S1])(rampaBase)))
ringhiera = GRID([[.05],[.05,-.05,.05,-.05,.05,-.05,.05,-.05,.05,-.05,.05,-.05,.05,-.05,.05,-.05,.05,-.05,.05,-.1,.05,-.05,.05,-.05,.05,-.05,.05,-.05,.05,-.05,.05,-.05,.05,-.05,.05,-.05,.05,-.05,.05],[1]])
passamano = GRID([[.05],[2],[-1,.05]])
supporto = STRUCT([ringhiera,passamano])
pianerottoloTerra = STRUCT([stairTerra,rampaTerra,muro_di_fondo,COLOR(BLACK)(T([1,2,3])([-3,-2,.3])(supporto))])
pianerottoloSuperiore = STRUCT([stair3D,muro_di_fondo,COLOR(BLACK)(T([1,2,3])([-3,-2,.3])(supporto)),COLOR(BLACK)(T([1,2,3])([-2,-3,.3])(MAP([S2,S1,S3])(supporto)))])
pianerottoli = STRUCT([pianerottoloTerra,T(3)(3)(pianerottoloSuperiore),T(3)(6)(pianerottoloSuperiore)])

#palazzina intera
floor1 = T(3)(3)(STRUCT([STRUCT(MKPOLS(master1)),finestre1,porta1]))
#VIEW(floor1)
floor2 = T(3)(3)(floor1)
roof = COLOR([0.545,0.27,0])(T([1,3])([-1,9])(CUBOID([14,11,.3])))
ala1 = STRUCT([floor0,out,floor1,floor2,roof])
ala2 = S(2)(-1)(ala1)
ala3 = T(1)(-2)(S(1)(-1)(ala1))
place = COLOR([.4,.4,.4])(T(3)(-0.1)(CYLINDER([20,0.1])(72)))

#elevatore
floor = COLOR(GREEN)(T([1,2,3])([-5,-5,-.1])(CUBOID([10,10,.1])))
g1 = T(3)(1)(MATERIAL([1,1,1,0.1, 0,0,0.8,0.5, 1,1,1,0.1, 1,1,1,0.1, 100])(floor))
elevator1 = ((T([1,2])([-3,-3.5])(CUBOID([1,1.5,3.3]))))
elevator2 = COLOR([.4,.4,.4])(((T([1,2,3])([-3,-3.5,3.3])(CUBOID([1,1.5,2.7])))))
elevator3 = ((T([1,2,3])([-3,-3.5,6])(CUBOID([1,1.5,3]))))
elevator1 = trasparenza(elevator1)
elevator3 = trasparenza(elevator3)
elevators = STRUCT([elevator1,elevator2,elevator3])

#piscina
WATERBLUE = [0.498,1,0.831]
#prima curva
controlpoints = [[0,0],[0,2*3],[-2*3,2*3],[-4*3,0],[0,-3*3]]
dom = larDomain([64])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
curva1 = STRUCT(MKPOLS(obj))
cuore1 = STRUCT([curva1,S(1)(-1)(curva1)])
#seconda curva
controlpoints = [[0,-.1*3],[0,2*3],[-1.8*3,1.9*3],[-4*3,0],[0,-2.9*3]]
dom = larDomain([64])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
curva2 = STRUCT(MKPOLS(obj))
cuore2 = STRUCT([curva2,S(1)(-1)(curva2)])
#terza curva
controlpoints = [[0,-.2*3],[0,2*3],[-1.6*3,1.8*3],[-4*3,0],[0,-2.8*3]]
dom = larDomain([64])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
curva3 = STRUCT(MKPOLS(obj))
cuore3 = STRUCT([curva3,S(1)(-1)(curva3)])
#quarta curva
controlpoints = [[0,-.3*3],[0,2*3],[-1.4*3,1.7*3],[-4*3,0],[0,-2.7*3]]
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
curva4 = STRUCT(MKPOLS(obj))
cuore4 = STRUCT([curva4,S(1)(-1)(curva4)])
#strati della piscina
esterno1 = PROD([SOLIDIFY(cuore1),Q(.4)])
esterno2 = PROD([SOLIDIFY(cuore2),Q(.1)])
esterno3 = PROD([SOLIDIFY(cuore3),Q(.1)])
base = PROD([SOLIDIFY(cuore4),Q(.2)])
acqua = PROD([SOLIDIFY(cuore4),Q(.1)])
#assemblaggio piscina
acqua = COLOR(WATERBLUE)(acqua)
bordo = DIFFERENCE([esterno1,T(3)(.3)(esterno2),T(3)(.2)(esterno3),base])
piscina = T([1,2])([-10,-8])(STRUCT([bordo,acqua]))

#collina
controlpoints = [[20,0],[22,0],[24,0],[26,-1],[28,-4],[29,-7],[30,-10]]
dom = larDomain([64])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
curva = STRUCT(MKPOLS(obj))
hill = STRUCT([curva,S(1)(-1)(curva),POLYLINE([[-20,0],[20,0]]),POLYLINE([[-30,-10],[30,-10]])])
hill2D = T(1)(-1.3)(MAP([S3,S1,S2])((PROD([SOLIDIFY(hill),Q(2.6)]))))
hill2D = COLOR([0.002,0.743,0.224])(hill2D)
hill3D = T(3)(-0.1)(STRUCT(NN(36)([hill2D,R([1,2])(PI/36)])))

palazzina = STRUCT([ala1,ala2,ala3,place,hill3D,elevators,pianerottoli,piscina])

print("Loading... Please Wait")
VIEW(palazzina)
