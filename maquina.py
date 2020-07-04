solucionCache = []
piezas = []
piezasSolucion = [] # Array de piezas colocadas
solucion = []

if existe solucion en cache:
	return solucionCache
def resolver():
	if len(piezasSolucion) > 0:
		if movimientoValido(): # Verifica la matriz solución contra la ultima pieza solucion guardada
			piezaGuardada=piezas.pop(0) # se tiene que volver a agregar en el backtraking (VERIFICAR)
			actualizarSolucion() # Agrega la ultima pieza de la lista piezas solucion a la matriz solución
		else:
			return
	if len(piezas) == 0:
		# guardar solución en cache
		return solucionCache
	for _ in range(len(piezas)):
		for _ in range(2): # voltee la pieza
			for _ in range(4): # Rotacion 90 grados
				colocarPieza()
				resolver()
				sacarPieza()
				rotarPieza() #rota de forma antihoraria
			voltearPieza()
	print("No existe solución")


def colocarPieza():
	pieza = piezas[0]
	p = obtenerPosInfIzq(pieza)
	s = obtenerPosInfIzq(solucion)
	ps = generarPieza(p, s) # Generar la pieza del tamaño del molde
	piezasSolucion.append(ps)

def sacarPieza():
	piezasSolucion.pop()

def rotarPieza(matriz):
	rotada=[]
	for i in range(len(matriz[0])):
		rotada.append([])
		for j in range(len(matriz)):
			rotada[i].append(matriz[len(matriz)-1-j][i])
	return rotada

def voltearPieza(matriz):
    matriz.reverse()
    return matriz

"""FUNCION GEMAS	
from collections import Counter

gema_roja=[1,1,1,1,1,1,1,1,1,1,1,1]
gema_azul=[2,2,2,2,2,2,2,2,2,2,2,2]
gema_morada=[3,3,3,3,3,3,3,3,3,3,3,3]
gema_rosada=[4,4,4,4,4,4,4,4,4,4,4,4]
gema_verde=[5,5,5,5,5,5,5,5,5,5,5,5]
gema_blanca=[6,6,6,6,6,6,6,6,6,6,6,6]


gemas = [[2,4,2,4,2,1,4,6,3,6,5,2],
		[2,1,4,3,2,4,1,2,5,5,4,3],
		[6,3,1,1,2,2,5,5,6,1,2,3],
		[1,3,5,5,2,6,5,6,3,6,2,3],
		[5,4,4,6,3,4,3,4,5,1,5,6],
		[1,3,1,6,1,4,3,4,6,5,6,1]]
	
#busca entre las filas la mayor cantidad de gemas de un color y se posiciona
#prioriza los colores que ya tiene agregado 
#si se puede desplazar busca la mejor final, sino la siguiente mejor mas proxima
def seleccionaGemas(gemas):
    for _ in range(2):
        x = mejorLugar(gemas)
        print(x)#prueba
        quitarPiezas(gemas,x)

def mejorLugar(gemas):
    repetidos=[]
    posicion = None
    for i in gemas:
        count = Counter(i)
        repetidos.append(max(count, key=count.get))
    for num1,i in enumerate(repetidos):
        for num2,j in enumerate(repetidos):
            if(num1!=num2 and i==j):
                posicion = num1
                return posicion

    return posicion

def quitarPiezas(gemas,x):
    gemas[x].pop(0)
    gemas[x].pop(1)
    gemas[x].pop(2)
    print(gemas)#prueba

seleccionaGemas(gemas)"""