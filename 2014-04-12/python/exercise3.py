# This Python file uses the following encoding: utf-8
from exercise1 import *
from exercise2 import *
from pyplasm import *

#assemblamento del tempio dagli esercizi precedenti

tempio = STRUCT([horizontal_partitions,vertical_enclosures])
#____________________________________________________________________________

#pavimentazione esterna
floor = T([1,2,3])([-50,-70,-0.1])(INSR(PROD)([QUOTE([100]),QUOTE([140]),QUOTE([0.1])]))

#il prato attorno al tempio
x = QUOTE([42.5])
y = QUOTE([62.5])
rect = INSR(PROD)([x,y,QUOTE([0.1])])
cyrc = CYLINDER([7.5,0.1])(36)
prato_base = (DIFFERENCE([rect,cyrc]))
prato1 = T([1,2])([5,5])(prato_base)
prato2 = S(2)(-1)(prato1)
prato3 = S(1)(-1)(prato1)
prato4 = S(1)(-1)(prato2)

pratone = STRUCT([prato1,prato2,prato3,prato4])

#gli edifici vicini
#edifica crea un edificio con x stanze per y stanze e con z piani
def edifica(x,y,z):
    xcoo = 5.4*(x+1) - 5
    ycoo = 5.4*(y+1) - 5
    zcoo = 3.3*z
    x_pilastri = QUOTE([0.4,-5]*(x+1))
    y_pilastri = QUOTE([0.4,-5]*(y+1))
    pilastri = INSR(PROD)([x_pilastri,y_pilastri,QUOTE([-0.3,3]*z)])
    x_piano = QUOTE([xcoo])
    y_piano = QUOTE([ycoo])
    piani = INSR(PROD)([x_piano,y_piano,QUOTE([0.3,-3]*(z+1))])
    return T(3)(0.1)(STRUCT([pilastri,piani]))

edificio1 = T([1,2])([14,15])(edifica(5,8,11))
edificio2 = T([1,2])([-44,40])(edifica(6,3,3))
edificio3 = T([1,2])([15,-55])(edifica(3,6,5))
edificio4a = T([1,2])([-45,-55])(edifica(6,6,2))
edificio4b = T([1,2,3])([-45,-55,6.3])(edifica(6,4,3))
edificio4c = T([1,2,3])([-45,-55,6.3])(edifica(4,6,3))
edificio4d = T([1,2,3])([-45,-55,16])(edifica(6,6,1))
#un albero nell'edificio 4
tronco = CYLINDER([0.2,1.5])(36)
tronco = COLOR([0.596,0.463,0.329])(tronco)
cono = JOIN([MK([0,0,4]),CYLINDER([2,0])(36)])
cono = COLOR([0.467,0.867,0.467])(cono)
base_albero = CYLINDER([0.5,0.1])(36)
base_albero = COLOR([0.896,0.763,0.629])(base_albero)
albero_edificio4 = T([1,2,3])([-17,-28,7])(STRUCT([base_albero,T(3)(0.1)(tronco),T(3)(1.6)(cono)]))

neighbouring_buildings = STRUCT([edificio1,edificio2,edificio3,edificio4a,edificio4b,edificio4c,edificio4d,albero_edificio4])

#colore
floor = COLOR([0.8,0.9,0.8])(floor)
pratone = COLOR([0.012,0.753,0.234])(pratone)
neighbouring_buildings = COLOR([0.596,0.463,0.329])(neighbouring_buildings)


#VIEW(STRUCT([floor,pratone,tempio,neighbouring_buildings]))
