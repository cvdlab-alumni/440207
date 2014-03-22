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

t = tegolator(8)
tt = MAP([S3,S2,S1])(t)
ttt = R([1,3])(PI*1.1)(tt)
c = copertura(ttt)

#se i tempi di caricamento sono lunghi scegliere l'istanza alternativa di "cono"
cono = T(3)(11.8)(c)
#cono = JOIN([tetto3top,MK([0,0,14.2])])

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

#restituisce l'i-esimo gradino su tot
def step(i,tot):
        g1 = ((i-1)*2*PI)/tot
        g2 = (i*2*PI)/tot
        punti = [[0,0,0],[2*COS(g1),2*SIN(g1),0],[2*COS(g2),2*SIN(g2),0],[0,0,(4+0.0)/tot],[2*COS(g1),2*SIN(g1),(4+0.0)/tot],[2*COS(g2),2*SIN(g2),(4+0.0)/tot]]
        tri = JOIN(AA(MK)(punti))
        return tri

#restituisce una scala a chiocciola alta 1 che compie 360° con n gradini
def gradini(n):
        output = step(0,n)
        for i in range(n-1):
                ef = R([1,2])(i*PI/(16*n))(step(i,n))
                eff = T(3)(i*3.0/n)(ef)
                output = STRUCT([output,eff])
        return output

#creo la scala per il naos
chiocciola = STRUCT([gradini(72),T(3)(2.95)]*3)
chiocciola = COLOR([0.957,0.643,0.376])(chiocciola)

VIEW(STRUCT([solid_model_3D,chiocciola]))
