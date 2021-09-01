import DatosGenerales as BD

#print(BD.primeraLetra.keys())

def obtenerLetra(Matricula,Op):
    Letra=''
    if Op == 1:
        Letra=Matricula[0]
        return Letra
    elif Op == 2:
        Letra=Matricula[1]
        return Letra
    elif Op == 3:
        Letra=Matricula[0:2]
        return Letra
    elif Op == 4:
        Letra=Matricula[2]
        return Letra

def validarPrimeraLetra(Matricula):
    lista=BD.primeraLetra
    Letra=obtenerLetra(Matricula,1)
    mensaje=False
    for (k,v) in lista.items():
        #print(k)
        if Letra==k:
            print("Provincia "+v +"\n")
            return True
    return mensaje  

def validarSegundaLetra(Matricula):
    lista=BD.segundaLetra
    
    Letra=obtenerLetra(Matricula,2)
    mensaje=False
    for (k,v) in lista.items():
        #print(k)
        if Letra==k:
            print("Tipo de matricula "+v+"\n")
            return True
    for k in range(1):
        if k == Letra:
            print("Tipo de matricula de uso personal\n")
            return True 
    return mensaje 

def validarMatriculaEspecial(Matricula):
    lista=BD.matriculaEspecial
    Letra=obtenerLetra(Matricula,3)
    mensaje=False
    for (k,v) in lista.items():
        #print(k)
        if Letra==k:
            print("Matricula Especial de tipo "+v  +"\n")
            return True
    return mensaje 

def validarTerceraLetra(Matricula):
    lista=BD.Abecedario
    Letra=obtenerLetra(Matricula,4)
    mensaje=False
    for k in lista:
        #print(k)
        if Letra==k:
            print("Tercera Letra Valida")
            return True
    return mensaje  

matri='ACB-123'
#print(validarPrimeraLetra(matri))
#print(validarSegundaLetra(matri))
#print(validarMatriculaEspecial(matri))
#print(validarTerceraLetra(matri))

#Pruebas Unitarias


