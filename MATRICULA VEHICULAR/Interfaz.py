import Funciones as fun

matricula=input('Ingrese las letras de la matricula en mayuscula:\n')
if matricula.isdigit():
    print('Ingrese letras no digitos\n')
elif matricula.isupper:
    if fun.validarMatriculaEspecial(matricula):
        numero=input('Digite los numero')
        matricula=matricula+numero
    elif fun.validarPrimeraLetra(matricula):
        if fun.validarSegundaLetra(matricula):
            if fun.validarTerceraLetra(matricula):
                numero=input('Digite los numero: ')
                if numero.isdigit():
                    if int(numero)<999:
                        matricula=matricula+"-"+numero
                        print(matricula)
                else:print("Digitos invalidos")
    else: print("Digitos invalidos")
        