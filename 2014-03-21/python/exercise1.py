from pyplasm import *

#per 20 volte, il cerchio viene traslato in una circonferenza di raggio 5
#il primo è posto a PI/20 per creare un intervallo in corrispondenza dell'asse x
def roundcircle():
	out = CIRCUMFERENCE(0)(1)
	l = CIRCUMFERENCE(0.25)(12)
	for i in range(20):
		a = T([1,2])([5*COS((PI/20)+(i*PI/10)), 5*SIN((PI/20)+(i*PI/10))])(l)
		out = STRUCT([out,a])
	return out

#per 20 volte il quadrato viene rototraslato in una circonferenza di raggio 5
#il primo è posto a PI/20 per creare un intervallo in corrispondenza dell'asse x
def roundsquare():
	out = CUBOID([0,0,0])
	c = CUBOID([0.7,0.7,0])
	l = T([1,2])([-0.35,-0.35])(c)
	for i in range(20):
		b = R([1,2])(PI/20 + i*PI/10)(l)
		a = T([1,2])([5*COS((PI/20)+(i*PI/10)),5*SIN((PI/20)+(i*PI/10))])(b)
		out = STRUCT([out,a])
	return out

#floor0 (gradini inferiori al colonnato)
step1 = CIRCUMFERENCE(7)(360)
step2 = CIRCUMFERENCE(6.5)(360)
step3 = CIRCUMFERENCE(6)(360)
base2D = CIRCUMFERENCE(5.5)(360)
floor0 = STRUCT([step1,step2,step3,base2D])

#floor1 (base del colonnato e della porta del naos)
squares2D = roundsquare()
naosClosed2D = DIFFERENCE([CYLINDER([3.25,0.001])(72),CYLINDER([3,0.001])(72)])
door = T([1,2])([2.5,-1])(CUBOID([1,2,0.001]))
naos2D = DIFFERENCE([naosClosed2D,door])
floor1 = STRUCT([squares2D,naos2D])

#floor2 (colonne e naos con finestre)
columns2D = SOLIDIFY(roundcircle())
window2D = T([1,2])([2.5,-0.35])(CUBOID([1,0.7,0.001]))
leftwindow2D = R([1,2])(-PI/3)(window2D)
rightwindow2D = R([1,2])(PI/3)(window2D)
windows2D = STRUCT([leftwindow2D,rightwindow2D])
naosWindows2D = DIFFERENCE([naosClosed2D,door,windows2D])
floor2 = STRUCT([columns2D,naosWindows2D])

#floor3 (sommità del colonnato e naos privo di porta e finestre)
floor3 = STRUCT([naosClosed2D,squares2D])

#floor4 (tetto)
floor4 = CIRCUMFERENCE(6.2)(360)

#ogni "piano" viene colorato nella scala di blu
floor0 = COLOR([0,0,1])(floor0)         #100% blu
floor1 = COLOR([0.2,0.2,1])(floor1)     #80% blu
floor2 = COLOR([0.4,0.4,1])(floor2)     #60% blu
floor3 = COLOR([0.6,0.6,1])(floor3)     #40% blu
floor4 = COLOR([0.8,0.8,1])(floor4)     #20% blu

#two_and_half_model (ogni piano viene trasposto sull'asse z relativo alla propria altezza di riferimento)
two_and_half_model = STRUCT([floor0,T(3)(1.2)(floor1),T(3)(4.2)(floor2),T(3)(8.2)(floor3),T(3)(9.4)(floor4)])


VIEW(two_and_half_model)
