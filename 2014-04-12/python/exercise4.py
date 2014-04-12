# This Python file uses the following encoding: utf-8

from pyplasm import *
from larcc import *
from exercise3 import *

def translatePoints (points, tvect): # d-dimensional
        return [VECTSUM([p,tvect]) for p in points]

def scalePoints (points, svect): # d-dimensional
        return [AA(PROD)(TRANS([p,svect])) for p in points]

def larDomain(shape):
        V,CV = larSimplexGrid(shape)
        V = scalePoints(V, [1./d for d in shape])
        return V,CV

def larIntervals(shape):
        def larIntervals0(size):
                V,CV = larDomain(shape)
                V = scalePoints(V, [scaleFactor for scaleFactor in size])
                return V,CV
        return larIntervals0

def larMap(coordFuncs):
        def larMap0(domain):
                V,CV = domain
                V = TRANS(CONS(coordFuncs)(V)) # plasm CONStruction
                return V,CV
        return larMap0

def larSphere(radius=1):
        def larSphere0(shape=[18,36]):
                V,CV = larIntervals(shape)([PI,2*PI])
                V = translatePoints(V,[-PI/2,-PI])
                domain = V,CV
                x = lambda V : [radius*COS(p[0])*SIN(p[1]) for p in V]
                y = lambda V : [radius*COS(p[0])*COS(p[1]) for p in V]
                z = lambda V : [radius*SIN(p[0]) for p in V]
                return larMap([x,y,z])(domain)
        return larSphere0

def larBall(radius=1):
        def larBall0(shape=[18,36]):
                V,CV = larSphere(radius)(shape)
                return V,[range(len(V))]
        return larBall0


#il primo gradino del tempio, come punto di riferimento
base_tempio = CYLINDER([7,0.3])(360)
#la base degli edifici, come punto di riferimento
edificio_1 = T([1,2,3])([14,15,0.1])(INSR(PROD)([QUOTE([5.4*(5+1)-5]),QUOTE([5.4*(8+1)-5]),QUOTE([0.1])]))
edificio_2 = T([1,2,3])([-44,40,0.1])(INSR(PROD)([QUOTE([5.4*(6+1)-5]),QUOTE([5.4*(3+1)-5]),QUOTE([0.1])]))
edificio_3 = T([1,2,3])([14.5,-55,0.1])(INSR(PROD)([QUOTE([5.4*(14+1)-5]),QUOTE([5.4*(6+1)-5]),QUOTE([0.1])]))
edificio_4 = T([1,2,3])([-45,-55,0.1])(INSR(PROD)([QUOTE([5.4*(6+1)-5]),QUOTE([5.4*(6+1)-5]),QUOTE([0.1])]))
edificio_5 = T([1,2,3])([125,30,0.1])(INSR(PROD)([QUOTE([5.4*(3+1)-5]),QUOTE([5.4*(3+1)-5]),QUOTE([0.1])]))
edifici = STRUCT([edificio_1,edificio_2,edificio_3,edificio_4,edificio_5])
#scenario 2D
scenario = COLOR([0.596,0.463,0.329])(STRUCT([floor,pratone,base_tempio,edifici]))

#gli elementi precedenti sono solo una base presa dall'esercizio 3
#per visualizzare in dettagli l'arredo urbano, successivamente
#verranno uniti i seguenti elementi al tempio e ai palazzi limitrofi
#_______________________________________________________________________________


#ARREDO URBANO
tronco = CYLINDER([0.2,1.5])(36)
tronco = COLOR([0.596,0.463,0.329])(tronco)
#albero a cono
cono = JOIN([MK([0,0,4]),CYLINDER([2,0])(36)])
cono = COLOR([0.467,0.867,0.467])(cono)
tree_cone = STRUCT([tronco,T(3)(1.5)(cono)])
#albero a palla
palla = STRUCT(MKPOLS(larBall(2.2)([18,36])))
palla = COLOR([0.467,0.867,0.467])(palla)
tree_ball = STRUCT([tronco,T(3)(3.5)(palla)])
#panchina (alta 1)
profilo_panchina = SOLIDIFY(POLYLINE([[0,0],[0.25,0],[0.25,0.75],[2.25,0.75],[2.25,0],[2.5,0],[2.5,1],[0,1],[0,0]]))
panchina = MAP([S1,S3,S2])(PROD([profilo_panchina,Q(0.6)]))
panchina = COLOR([0.5,0.5,0.5])(panchina)
#lampione (alto 1.5)
lamp_base = CYLINDER([0.1,1.5])(36)
faroSx_up = T([1,3])([0.25,1.4])(CYLINDER([0.1,0.1])(36))
faroSx_mid = T([1,3])([0.25,1.3])(CYLINDER([0.1,0.1])(36))
faroSx_down = T([1,3])([0.25,1.2])(CYLINDER([0.1,0.1])(36))
faroDx_up = T([1,3])([-0.25,1.4])(CYLINDER([0.1,0.1])(36))
faroDx_mid = T([1,3])([-0.25,1.3])(CYLINDER([0.1,0.1])(36))
faroDx_down = T([1,3])([-0.25,1.2])(CYLINDER([0.1,0.1])(36))
connettivo = T([1,2,3])([-0.2,-0.025,1.4])(CUBOID([0.5,0.05,0.05]))
faro_luce = STRUCT([faroSx_mid,faroDx_mid])
faro_struttura = STRUCT([lamp_base,faroSx_up,faroSx_down,faroDx_up,faroDx_down,connettivo])
faro_luce = COLOR([1,1,0.4])(faro_luce)
faro_struttura = COLOR([0.2,0.2,0.2])(faro_struttura)
faro = STRUCT([faro_luce,faro_struttura])
#cestino (alto 1)
cestino_base = CIRCUMFERENCE(0.2)(36)
cestino_sommita = T(3)(0.5)(CIRCUMFERENCE(0.3)(36))
cestino_pieno = JOIN([cestino_base,cestino_sommita])
cestino = DIFFERENCE([cestino_pieno,T(3)(0.01)(cestino_pieno)])
cestino = COLOR([0.388,0.592,0.816])(cestino)
#piscina ovale
bordo1a = CYLINDER([6,0.3])(48)
bordo1b = CYLINDER([5.9,0.3])(48)
bordo1 = DIFFERENCE([bordo1a,bordo1b])
bordo2a = CYLINDER([5.9,0.2])(48)
bordo2b = CYLINDER([5.8,0.2])(48)
bordo2 = DIFFERENCE([bordo2a,bordo2b])
acqua = CYLINDER([5.8,0.1])(48)
acqua = COLOR([0.498,1,0.831])(acqua)
piscina_tonda = STRUCT([bordo1,bordo2,acqua])
piscina_ovale = T([1,2,3])([-28,25,0.1])(S(1)(2)(piscina_tonda))
#piscina rettangolare
bordo3a = CUBOID([32,55,0.3])
bordo3b = T([1,2])([0.5,0.5])(CUBOID([31,54,0.3]))
bordo3 = DIFFERENCE([bordo3a,bordo3b])
bordo4a = CUBOID([31,54,0.2])
bordo4b = T([1,2])([0.5,0.5])(CUBOID([30,53,0.2]))
bordo4 = DIFFERENCE([bordo4a,bordo4b])
acqua = T([1,2])([1,1])(CUBOID([30,53,0.1]))
acqua = COLOR([0.498,1,0.831])(acqua)
piscina_rettangolare = STRUCT([bordo3,T([1,2])([0.5,0.5])(bordo4),acqua])
piscina_rettangolare = T([1,2,3])([118,-65,0.1])(piscina_rettangolare)

#popola un rettangolo(giardino) con alberi a cono e sferici
def popola(n):
    oggetti = T([1,2])([21.25,31.25])(cestino)
    for i in range(n):
        oggetti = STRUCT([oggetti,T([1,2])([random.random()*42.5,random.random()*62.5])(tree_ball)])
        oggetti = STRUCT([oggetti,T([1,2])([random.random()*42.5,random.random()*62.5])(tree_cone)])
    return T(3)(0.1)(oggetti)

#posizionamento arredi
faro_tempio = T([1,2])([5.5,5.5])(R([1,2])(-PI/4)(faro))
faro1 = T([1,2,3])([15,7.5,0.1])(faro)
panchina1 = T([1,2])([20,4])(panchina)
albero1 = T([1,2,3])([21.2,7.5,0.1])(tree_ball)
cestino1 = T([1,2])([27,4])(cestino)
#prima e seconda fila di oggetti
arredo_urbano_fila_a = STRUCT([faro1,panchina1,albero1,cestino1])
arredo_urbano_fila_b = T(1)(12.15)(arredo_urbano_fila_a)
arredo_urbano_fila1 = STRUCT([faro_tempio,arredo_urbano_fila_a,arredo_urbano_fila_b])
#unisco e replico per gli arredi di una strada
arredo_urbano_fila2 = S(2)(-1)(arredo_urbano_fila1)
arredo_urbano_strada1 = STRUCT([arredo_urbano_fila1,arredo_urbano_fila2])
#replico per la strada 2..
arredo_urbano_strada2 = S(1)(-1)(arredo_urbano_strada1)
#..la strada 3(aggiungo una terza e quarta fila poichè la strada è più lunga)..
arredo_urbano_fila_c = STRUCT([faro1,panchina1,albero1,cestino1])
arredo_urbano_fila_d = T(1)(12.15)(arredo_urbano_fila_c)
arredo_urbano_fila_e = T(1)(12.15)(arredo_urbano_fila_d)
arredo_urbano_fila_f = T(1)(12.15)(arredo_urbano_fila_e)
arredo_urbano_fila3 = STRUCT([arredo_urbano_fila_c,arredo_urbano_fila_d,arredo_urbano_fila_e,arredo_urbano_fila_f])
arredo_urbano_fila4 = S(2)(-1)(arredo_urbano_fila3)
arredo_urbano_strada3 = R([1,2])(PI/2)(STRUCT([arredo_urbano_fila3,arredo_urbano_fila4]))
#..e la strada 4
arredo_urbano_strada4 = S(2)(-1)(arredo_urbano_strada3)
#unisco il tutto e aggiungo gli alberi nella piazza
albero1 = T([1,2])([12,12])(tree_cone)
albero2 = T([1,2])([-12,12])(tree_cone)
albero3 = T([1,2])([12,-12])(tree_cone)
albero4 = T([1,2])([-12,-12])(tree_cone)
bosco = T([1,2])([57.5,5])(popola(150))
arredo_urbano1 = STRUCT([arredo_urbano_strada1,arredo_urbano_strada2,arredo_urbano_strada3,arredo_urbano_strada4,albero1,albero2,albero3,albero4])
arredo_urbano2 = T(1)(105)(arredo_urbano1)
arredo_urbano3 = T(1)(52.5)(STRUCT([arredo_urbano_strada3]))
arredo_urbano = STRUCT([arredo_urbano1,arredo_urbano2,arredo_urbano3,piscina_ovale,piscina_rettangolare,bosco])

#selezionare solo una delle due VIEW seguenti
#VIEW(STRUCT([scenario,arredo_urbano]))
VIEW(STRUCT([floor,pratone,arredo_urbano,tempio,neighbouring_buildings]))
