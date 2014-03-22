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

#naos (con porta e finestre)
naosChiuso = T(3)(1.2)(DIFFERENCE([(CYLINDER([3.5,7])(120)),(CYLINDER([3,7])(120))]))
portaBot = T([1,2,3])([2.5,-1,1.2])(CUBOID([1,2,5]))
portaTop = T([1,3])([2.5,6.2])(MAP([S3,S2,S1])(CYLINDER([1,1])(36)))
porta = STRUCT([portaBot,portaTop])
finestra = T([1,2,3])([2.5,-0.5,3.5])(CUBOID([1,1,2]))
finestraSx = R([1,2])(-PI/3)(finestra)
finestraDx = R([1,2])(PI/3)(finestra)
naos = DIFFERENCE([naosChiuso,porta,finestraSx,finestraDx])

#tetto (con vari soffitti)
tetto1 = T(3)(8.2)(CYLINDER([5.5,0.6])(72))
tetto2bot = T(3)(8.8)(CIRCUMFERENCE(5.5)(72))
tetto2top = T(3)(9.1)(CIRCUMFERENCE(6)(72))
tetto2 = JOIN([tetto2bot,tetto2top])
tetto3bot = T(3)(9.1)(CIRCUMFERENCE(6.5)(72))
tetto3top = T(3)(9.4)(CIRCUMFERENCE(6.7)(36))
tetto3 = JOIN([tetto3bot,tetto3top])

cono = JOIN([tetto3top,MK([0,0,14.2])])

#circonferenzaCono = T(3)(9)(CIRCUMFERENCE(7.6)(36))
#conoTop = JOIN([circonferenzaCono,MK([0,0,14])])
#conoBot = T(3)(-0.1)(conoTop)
#cono = DIFFERENCE([conoTop,conoBot])
#cono = COLOR([0.396,0.263,0.129])(cono)

tetto = STRUCT ([tetto1,tetto2,tetto3])

#prato
prato = CYLINDER([15,0])(10)

#colori (rigorosamente pastello)
gradinataCircolare = COLOR([0.761,0.698,0.502])(gradinataCircolare)
colonnato = COLOR([0.761,0.698,0.502])(colonnato)
naos = COLOR([0.761,0.698,0.502])(naos)
tetto = COLOR([0.761,0.698,0.502])(tetto)
cono = COLOR([0.396,0.263,0.129])(cono)
prato = COLOR([0.012,0.753,0.234])(prato)

solid_model_3D = STRUCT([gradinataCircolare,colonnato,naos,tetto,cono,prato])

VIEW(solid_model_3D)
