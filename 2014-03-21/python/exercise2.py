from pyplasm import *

#per 20 volte, ogni oggetto viene rototraslato in una circonferenza di raggio 5
#il primo è posto a PI/20 per creare un intervallo in corrispondenza dell'asse x
def circling(l):
	out = l
	for i in range(20):
		b = R([1,2])(PI/20 + i*PI/10)(l)
		a = T([1,2])([5*COS((PI/20)+(i*PI/10)),5*SIN((PI/20)+(i*PI/10))])(b)
		out = STRUCT([out,a])
	out = DIFFERENCE([out,l])
	return out

#restituisce un oggetto ruotato più volte su se stesso
def around(bone):
        out = bone
        for i in range(10):
                a = R([1,2])(i*PI/10)(bone)
                out = STRUCT([out,a])
        return out

#creazione delle colonne
columnStandard = T(3)(1.4)(CYLINDER([0.25,6.6])(24))
pedestalBot = T([1,2,3])([-0.35,-0.35,1.2])(CUBOID([0.7,0.7,0.2]))
pedestalTop = T([1,2,3])([-0.35,-0.35,8])(CUBOID([0.7,0.7,0.2]))
column = STRUCT([columnStandard,pedestalBot,pedestalTop])
columnsFacade = SKELETON(1)(circling(column))
columnsFacade2D = S(2)(0)(T(3)(1.2)(columnsFacade))

#creazione del profilo della scalinata circolare in 2D
step01 = POLYLINE([[-7,0,0],[-7,0,0.3],[7,0,0.3],[7,0,0],[-7,0,0]])
step02 = POLYLINE([[-6.5,0,0.3],[-6.5,0,0.6],[6.5,0,0.6],[6.5,0,0.3],[-6.5,0,0.3]])
step03 = POLYLINE([[-6,0,0.6],[-6,0,0.9],[6,0,0.9],[6,0,0.6],[-6,0,0.6]])
base02D = POLYLINE([[-5.5,0,0.9],[-5.5,0,1.2],[5.5,0,1.2],[5.5,0,0.9],[-5.5,0,0.9]])
steps = STRUCT([step01,step02,step03,base02D])

#creazione del naos in 2D
naos02 = POLYLINE([[-3.5,0,1.2],[-3.5,0,7.2],[3.5,0,7.2],[3.5,0,1.2],[-3.5,0,1.2]])

#creazione del profilo del tetto in 2D
preRoof1 = POLYLINE([[-5.5,0,8.2],[-5.5,0,8.5],[5.5,0,8.5],[5.5,0,8.2],[-5.5,0,8.2]])
preRoof2 = POLYLINE([[-5.5,0,8.5],[-5.5,0,8.8],[5.5,0,8.8],[5.5,0,8.5],[-5.5,0,8.5]])
preRoof3 = POLYLINE([[-5.5,0,8.8],[-6,0,9.1],[6,0,9.1],[5.5,0,8.8],[-5.5,0,8.8]])
preRoof4 = POLYLINE([[-6,0,9.1],[-6.2,0,9.4],[6.2,0,9.4],[6,0,9.1],[-6,0,9.1]])
roof = POLYLINE([[-6.2,0,9.4],[0,0,14.2],[6.2,0,9.4],[-6.2,0,9.4]])
ups = STRUCT([preRoof1,preRoof2,preRoof3,preRoof4,roof])

#north (back)
north = STRUCT([columnsFacade2D,steps,naos02,ups])

#south (front)
doorBot = (T([1,3])([-1,1.2])(CUBOID([2,0.001,5])))
doorTop = T(3)(6.2)(R([2,3])(PI/2)(CIRCUMFERENCE(1)(36)))
door2D = SKELETON(1)(STRUCT([doorBot,doorTop]))
window = SKELETON(1)(T([1,2,3])([-0.35,-3.5,3.5])(CUBOID([0.7,0.001,2])))
leftWindow = S(2)(0)(R([1,2])(-PI/3)(window))
rightWindow = S(2)(0)(R([1,2])(PI/3)(window))
south = STRUCT([north,door2D,leftWindow,rightWindow])

#east (right side)
east = STRUCT([north,leftWindow])

#west (left side)
west = STRUCT([north,rightWindow])

#essendo un tempio a base circolare, non si potranno avere 4 facciate da unire a two_and_half_model,
#si potrà però unire la facciata esterna vista da 10 angolazioni diverse (ognuna ruotata di PI/10 grazie al metodo around):

bicolumns = STRUCT([T(1)(-5.25)(CYLINDER([0.25,7])(12)),T(1)(5.25)(CYLINDER([0.25,7])(12))])
bicolumns2D = S(2)(0)(T(3)(1.2)(SKELETON(1)(bicolumns)))
bone = STRUCT([bicolumns2D,steps,naos02,ups])
roundBone = around(bone)

VIEW(roundBone)

#mock_up_3D = STRUCT([roundBone,two_and_half_model])  #mock_up_3D sarà composto dai vari livelli del tempio intersecati con le facciate ruotate dello stesso
