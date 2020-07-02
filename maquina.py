solucionCache = []
piezas = []
piezasSolucion = [] # Array de piezas colocadas
solucion = []
piezaGuardada = []

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