import numpy as np

def suma(c1, c2):
    """
    Suma dos numeros complejos
    :list c1: Lista de dos items, el primero es la parte real y la segunda es la parte imaginaria
    :list c2: Lista de dos items, el primero es la parte real y la segunda es la parte imaginaria
    :return list:
    """
    representacionSumaNumerosComplejos = [c1[0] + c2[0], c1[1] + c2[1]]
    return representacionSumaNumerosComplejos

def sumaMatrices(m1, m2):
    """
    Adds two complex matrices
    :Array m1: Matrix of n*m dimentions, each item is a complex number
    :Array m2: Matrix of n*m dimentions, each item is a complex number
    :return Array:
    """
    representacionSumaMatricesComplejas = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[i])):
            fila.append(suma(m1[i][j], m2[i][j]))
        representacionSumaMatricesComplejas.append(fila)
    return representacionSumaMatricesComplejas

def multiplicacion(c1, c2):
    """
    Funcion que multiplica dos numeros complejos
    :list c1: Lista de dos items, el primero es la parte real y la segunda es la parte imaginaria
    :list c2: Lista de dos items, el primero es la parte real y la segunda es la parte imaginaria
    :return list:
    """
    representacionMultiplicacionComplejos = [round(c1[0]*c2[0] - c1[1]*c2[1], 3), round(c1[0]*c2[1] + c1[1]*c2[0], 3)]
    return representacionMultiplicacionComplejos

def modulo(c):
    """
    Funcion que retorna el modulo de un numero complejo
    :lista c: Lista de dos items, el primero es la parte real y la segunda es la parte imaginaria
    :return float:
    """
    representacionModuloComplejo = (c[0] ** 2 + c[1] ** 2) ** 0.5
    return round(representacionModuloComplejo, 3)

def normaVector(v):
    """
    Funcion que retorna la norma de un vector complejo
    :Array v: Arreglo de n items, cada item es un numero complejo
    :return Float:
    """
    representacionNormaVectorComplejo = 0
    for i in range(len(v)):
        representacionNormaVectorComplejo += (modulo(v[i]) ** 2)
    return round(representacionNormaVectorComplejo ** 0.5, 2)

def transpuestaMatriz(m):
    """
    Funcion que retorna la transpuesta de una matriz
    :Matriz m: Arreglo de n*m items
    :return:
    """
    representacionTranspuestaMatriz = []
    for i in range(len(m[0])):
        fila = []
        for j in range(len(m)):
            fila += [m[j][i]]
        representacionTranspuestaMatriz += [fila]
    return representacionTranspuestaMatriz

def productoInterno(v1, v2):
    """
    Funcion que retorna el producto punto entre dos vectores
    :Array v1: Arreglo de n items, cada item es un numero complejo
    :Array v2: Arreglo de n items, cada item es un numero complejo
    :return Array:
    """
    if len(v1) == len(v2):
        representacionProductoPunto = [0, 0]
        for i in range(len(v1)):
            representacionProductoPunto = suma(representacionProductoPunto, multiplicacion(v1[i], v2[i]))
        return representacionProductoPunto
    else:
        return 'Not possible'

def multiplicarMatrices(m1, m2):
    """
    Función que multiplica dos matrices
    :Matriz m1: Arreglo de n*m items, cada item es un numero complejo
    :Matriz m2: Arreglo de n*m items, cada item es un numero complejo
    :return Array:
    """
    if len(m1[0]) == len(m2):
        representacionMultiplicacionMatrices = [[[0, 0] for j in range(len(m2[0]))] for i in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    representacionMultiplicacionMatrices[i][j] = suma(representacionMultiplicacionMatrices[i][j], multiplicacion(m1[i][k], m2[k][j]))
        return representacionMultiplicacionMatrices
    else:
        return 'Not possible'
def inversoAditivoMatrizCompleja(m):
    """
    Funcion que retorna el inverso aditivo de una matriz compleja
    :Matriz m: Matriz de n*m items, cada item es un numero complejo
    :return Array:
    """
    representacionInversoAditivoMatriz = []
    for i in range(len(m)):
        representacionInversoAditivoMatriz.append([])
        for j in range(len(m[i])):
            representacionInversoAditivoMatriz[i].append(multiplicacion(m[i][j], [-1, 0]))
    return representacionInversoAditivoMatriz

def conjugadaMatriz(m):
    """
    Funcion que retorna la conjugada de una matriz
    :Matriz m : Arreglo de n*m items, cada item es un numero complejo
    :return Array:
    """
    representacionConjugadaMatriz = m[::]
    for i in range(len(representacionConjugadaMatriz)):
        for j in range(len(representacionConjugadaMatriz[i])):
            aux = representacionConjugadaMatriz[i][j]
            aux[1] *= -1
    return representacionConjugadaMatriz

def adjuntaMatriz(m):
    """
    Funcion que retorna la adjunta de una matriz
    :Matriz m: Arreglo de n*m items, cada item es un numero complejo
    :return Array:
    """
    representacionAdjuntaMatriz = m[::]
    return transpuestaMatriz(conjugadaMatriz(representacionAdjuntaMatriz))

def esUnitariaMatriz(m):
    """
    Funcion que verifica que una matriz es unitaria
    :Matriz m: Arreglo de n*m items, cada item es un numero complejo
    :return Array:
    """
    if len(m) == len(m[0]):
        identificador = [[[0, 0] for j in range(len(m[0]))] for i in range(len(m))]
        for i in range(len(m)):
            for j in range(len(m[0])):
                if i == j:
                    identificador[i][j] = [1, 0]
        aux = adjuntaMatriz(m)
        producto = multiplicarMatrices(aux, m)
        representacionEsUnitaria = True
        for i in range(len(m)):
            for j in range(len(m)):
                if producto[i][j] != identificador[i][j]:
                    representacionEsUnitaria = False
        if representacionEsUnitaria:
            return True
        else:
            return False
    else:
        return False

#-----------------------------------------------------------------------

# El sistema calcula la probabilidad de encontrarlo en una posición en particular.
def probabilidadPosicionParticular(ket, position):
    numerador = modulo(ket[position]) ** 2
    denominador = normaVector(ket) ** 2
    return round(numerador/denominador, 3)


def bra(ket):
    for num in ket:
        if isinstance(num, list):
            num[1] *= -1
        else:
            num *= -1
    return ket

#2. Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación
def probabilidadTransicion(ket1, ket2):
    braket2 = bra(transpuestaMatriz(ket2)[0])
    norm1 = normaVector(transpuestaMatriz(ket1)[0])
    norm2 = normaVector(transpuestaMatriz(ket2)[0])
    norm = norm1 * norm2
    aux = transpuestaMatriz(ket1)
    prob = productoInterno(braket2, transpuestaMatriz(ket1)[0])
    ans = multiplicacion([1/norm, 0], prob)
    return ans


# 3. Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.
def varianza(observable, ket):
    brket = bra(ket)
    medVar = media(observable, ket)
    iMedVar = [[(0, 0) for j in range(len(observable[0]))] for i in range(len(observable))]
    for i in range(len(observable)):
        for j in range(len(observable[i])):
            if i == j:
                iMedVar[i][j] = inversoAditivoMatrizCompleja(medVar)
    iMedVar = sumaMatrices(iMedVar, observable)
    aux = multiplicarMatrices(iMedVar, iMedVar)
    representacionVar1 = multiplicarMatrices(aux, ket)
    representacionVar2 = productoInterno(representacionVar1, brket)
    return representacionVar2

def media(observable, ket):
    bra_ket = bra(ket)
    res1 = multiplicarMatrices(observable, ket)
    res2 = productoInterno(res1, bra_ket)
    return res2
#4. El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.
def vectorEigenValores(matrix):
    evalores, evectores = np.linalg.eig(matrix)
    valores = []
    vectores = []
    for i in range(len(evalores)):
        valores += [(evalores[i].real, evalores[i].imag)]
    for i in range(len(evectores)):
        vector = []
        for j in range(len(evectores[0])):
            vector += [(evectores[i][j].real, evectores[i][j].imag)]
        vectores += [vector]
    return valores, vectores

#5. Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado final a partir de un estado inicial.
def dinamica(mU, v1, t):
    if esUnitariaMatriz(mU):
        for index in range(t):
            v1 = multiplicarMatrices(mU, v1)
        return v1
    else:
        return "Matriz no valida"

# Ejercicios
# 4.3.1
def ejercicio1():
    vector = [[[1, 0]], [[0, 0]]]
    observable = [[[0, 0], [1, 0]], [[1, 0], [0, 0]]]
    observation = multiplicarMatrices(observable, vector)
    values, vectors = vectorEigenValores(observable)
    print('Resultado de la obervación: ', observation)
    print('Eigen Valores: ', values)
    print('Eigen Vectores: ', vectors)


# 4.3.2
def ejercicio2():
    vector = [[[1, 0]], [[0, 0]]]
    observable = [[[0, 0], [1, 0]], [[1, 0], [0, 0]]]
    values, vectors = vectorEigenValores(observable)
    for i in range(len(vectors)):
        print(probabilidadTransicion(vector, vectors[i]))


# 4.4.1
def ejercicio3():
    matrix1 = [[[0, 0], [1, 0]], [[1, 0], [0, 0]]]
    matrix2 = [[[(2**(1/2))/2, 0], [(2**(1/2))/2, 0]], [[(2**(1/2))/2, 0], [-(2**(1/2))/2, 0]]]
    if esUnitariaMatriz(matrix1) and esUnitariaMatriz(matrix2):
        print(esUnitariaMatriz(multiplicarMatrices(matrix1, matrix2)))

# 4.4.2
def ejercicio4():
    print(dinamica([[(0, 0), (1/(2**(1/2)), 0), (1/(2**(1/2)), 0), (0, 0)],[(1/(2**(1/2)), 0), (0, 0), (0, 0), (1/(2**(1/2)), 0)],[(1 / (2 ** (1 / 2)), 0), (0, 0), (0, 0), (1 / (2 ** (1 / 2)), 0)],
                        [(0, 0), (1/(2**(1/2)), 0), (1/(2**(1/2)), 0), (0, 0)]],[(1,0), (0,0), (0,0), (0,0)], 3))

print('Point 1')
ejercicio1()
print()
print('Point 2')
ejercicio2()
print()
print('Point 3')
ejercicio3()
print()
print('Point 4')
#ex4()

