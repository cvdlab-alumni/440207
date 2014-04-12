# This Python file uses the following encoding: utf-8

from pyplasm import *

#ruota un oggetto a 360°
def copertura(l):
	out = l
	for i in range(72):
		b = R([1,2])(i*PI/36)(l)
		out = STRUCT([out,b])
	return out

#restituisce una fila di tegole
def tegolator(n):
    tegola = DIFFERENCE([CYLINDER([0.3,1])(12),T(1)(0.1)(CYLINDER([0.3,1])(6))])
    output = tegola
    for i in range(n):
        occ = T([1,3])([0.1,(i+1)*0.9])(R([1,3])(-PI/36)(tegola))
        output = STRUCT([output,occ])
    return output

#naos (con porta e finestre)
naosChiuso = T(3)(1.2)(DIFFERENCE([(CYLINDER([3.5,7])(120)),(CYLINDER([3,7])(120))]))
portaBot = T([1,2,3])([2.5,-1,1.2])(CUBOID([1,2,5]))
portaTop = T([1,3])([2.5,6.2])(MAP([S3,S2,S1])(CYLINDER([1,1])(36)))
porta = STRUCT([portaBot,portaTop])
finestra = T([1,2,3])([2.5,-0.5,3.5])(CUBOID([1,1,2]))
finestraSx = R([1,2])(-PI/3)(finestra)
finestraDx = R([1,2])(PI/3)(finestra)
naos = DIFFERENCE([naosChiuso,porta,finestraSx,finestraDx])

#tegole
tegole = tegolator(8)
tegole_mappate = MAP([S3,S2,S1])(tegole)
tegole_ruotate = R([1,3])(PI*1.1)(tegole_mappate)
tegolato_base = copertura(tegole_ruotate)

#se i tempi di caricamento sono lunghi scegliere l'istanza alternativa di "tegolato"
#tegolato = T(3)(11.8)(tegolato_base)

tetto3top = T(3)(9.4)(CIRCUMFERENCE(6.7)(36))
tegolato = JOIN([tetto3top,MK([0,0,14.2])])

#colori (rigorosamente pastello)
naos = COLOR([0.561,0.498,0.302])(naos)
tegolato = COLOR([0.396,0.263,0.129])(tegolato)

vertical_enclosures = STRUCT([naos,tegolato])

#VIEW(vertical_enclosures)
