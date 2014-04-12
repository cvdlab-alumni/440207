# This Python file uses the following encoding: utf-8

from pyplasm import *

#per 20 volte, ogni oggetto viene rototraslato in una circonferenza di raggio 5
#il primo è posto a PI/20 per ottenere l'intervallo in corrispondenza dell'asse x
def circling(l):
	out = l
	for i in range(20):
		b = R([1,2])(PI/20 + i*PI/10)(l)
		a = T([1,2])([5*COS((PI/20)+(i*PI/10)),5*SIN((PI/20)+(i*PI/10))])(b)
		out = STRUCT([out,a])
	out = DIFFERENCE([out,l])
	return out

#base circolare (scale)
gradino1 = CYLINDER([7,0.3])(360)
gradino2 = T(3)(0.3)(CYLINDER([6.5,0.3])(72))
gradino3 = T(3)(0.6)(CYLINDER([6,0.3])(72))
gradinoBase = T(3)(0.9)(CYLINDER([5.5,0.3])(72))
gradinataCircolare = STRUCT([gradino1,gradino2,gradino3,gradinoBase])

#colonne (24 sezioni)
piedistalloBot = T([1,2,3])([-0.35,-0.35,1.2])(CUBOID([0.7,0.7,0.2]))
piedistalloTop = T([1,2,3])([-0.35,-0.35,8])(CUBOID([0.7,0.7,0.2]))
colonna = T(3)(1.4)(CYLINDER([0.25,6.6])(24))
colonnaTipo = STRUCT([piedistalloBot,colonna,piedistalloTop])
colonnato = circling(colonnaTipo)

#tetto (con vari soffitti)
tetto1 = T(3)(8.2)(CYLINDER([5.5,0.6])(72))
tetto2bot = T(3)(8.8)(CIRCUMFERENCE(5.5)(72))
tetto2top = T(3)(9.1)(CIRCUMFERENCE(6)(72))
tetto2 = JOIN([tetto2bot,tetto2top])
tetto3bot = T(3)(9.1)(CIRCUMFERENCE(6.5)(72))
tetto3top = T(3)(9.4)(CIRCUMFERENCE(6.7)(36))
tetto3 = JOIN([tetto3bot,tetto3top])
tetto = STRUCT ([tetto1,tetto2,tetto3])


#colori (rigorosamente pastello)
gradinataCircolare = COLOR([0.761,0.698,0.502])(gradinataCircolare)
colonnato = COLOR([0.561,0.498,0.302])(colonnato)
tetto = COLOR([0.361,0.298,0.102])(tetto)

horizontal_partitions = STRUCT([gradinataCircolare,colonnato,tetto])

#VIEW(horizontal_partitions)
