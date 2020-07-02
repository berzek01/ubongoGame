solucionCache = []
piezas = []
piezasSolucion = []

def resolver():
	if existe solucion:
		return solucionCache
	if len(piezasSolucion) > 0:
		if movimientoValido(): # Verifica la matriz solución contra la ultima pieza solucion guardada
			piezas.pop(0)
			llenarPuzle() # Agrega la ultima pieza a la matriz solución
		else:
			return
	if len(piezas) == 0:
		# guardar solución en cache
		return solucionCache
	for _ in range(piezas):
		for _ in range(2):
			for _ in range(4):
				colocarPieza()
				resolver()
				sacarPieza()
				rotarPieza()
			voltearPieza()
	print("No existe solución")


def colocarPieza():
	pieza = piezas[0]
	p = obtenerPosInfIzq(pieza)
	s = obtenerPosInfIzq(solucion)
	ps = generarPieza(p, s)
	solucion.append(ps)

def sacarPieza():
	solucion.pop()