
def experto(arbol):
    
    Nodoactual = arbol
    while len(Nodoactual) == 3:
        [pregunta, yesNode, noNode] = Nodoactual # nombre de atributos de la lista
        if aceptar(pregunta):
            Nodoactual = yesNode
        else: 
            Nodoactual = noNode
          
    [resultado] = Nodoactual
    if aceptar("Existe gran probabilidad de que tengas {}".format(resultado)):
		if (format(resultado)== 'Neumonia'):
			print("No olvides tomar tus antibioticos !\nEspero que te mejores !")
		if (format(resultado)== 'Gripe'):
			print("No olvides tomar tus pastas de acetaminofen !\nEspero que te mejores !")
		if (format(resultado)== 'Resfriado Comun'):
			print("No olvides tomar tus pastas de acetaminofen !\nEspero que te mejores !")	
		if (format(resultado)== 'Asma'):
			print("No olvides tomar tus pastas de Metaproterenol o Terbutalina !\nEspero que te mejores !")
		if (format(resultado)== 'Bronquitis'):
			print("No olvides tomar tus antibioticos !\nEspero que te mejores !")	
		if (format(resultado)== 'Influenza'):
			print("No olvides tomar tus pastas de ibuprofeno y trata de ir al medico  !\nEspero que te mejores !")
		if (format(resultado)== 'Amigdalitis'):
			print("No olvides tomar tus antibioticos !\nEspero que te mejores !")
		if (format(resultado)== 'Migrana'):
			print("No olvides tomar tus pastas de acetaminofen o advil !\nEspero que te mejores !")
		if (format(resultado)== 'Malestar General'):
			print("No olvides tomar un descanso !\nEspero que te mejores !")
		
    else: 
        nuevoresultado = raw_input("Entonces en que piensas? ")
        NuevaPregunta = raw_input('Que podria preguntar para que fuera verdad?\n'+
                            '  {} pero no para una {}? '.format(resultado, nuevoresultado))
        newYesNode = [resultado]
        newNoNode = [nuevoresultado]
        #Nodoactual[:] =... remplaza el contenido por un Nodoactual
        Nodoactual[:] = [NuevaPregunta, newYesNode, newNoNode] 
        print("Gracias por ensenarme algo nuevo!")

def aceptar(pregunta):
    '''retorna verdad si el usuario afirma.'''
    respuesta = raw_input(pregunta + ' (y/n) ')
    return respuesta.startswith('y')

def Buscar(arbol, indent='', dif='  '):
	'''cada nodo muestra la pregunta o la primera respuesta.
	'''
	if len(arbol) == 1:
		return indent + repr(arbol) 
	[pregunta, t1, t2,t3,t4] = arbol
	t1Str = Buscar(t1, indent+dif)
	t2Str = Buscar(t2, indent+dif)
	t3Str = Buscar(t3, indent+dif)
	t4Str = Buscar(t4, indent+dif)

	return '''{indent}[{pregunta!r},
	{t1Str},
	{t2Str},
	{t3Str},
	{t4Str}
	{indent}]'''.format(**locals())

def main():
    
    arbol = eval(fileToStr('enfermedades.txt')) #evalua el archivo
    #print("\nUsando este sistema experto:\n")
    #print(Buscar(arbol))
    mas = True
    while mas:
        experto(arbol)
        mas = aceptar('\nQuieres usar el sistema experto nuevamente?')
    print("\nEl sistema experto ahora es:\n")
    print(Buscar(arbol))    
    Guardararbol(arbol, fileName)
    
def Guardararbol(arbol,fileName):
    '''opcion para guardar el sistema experto:
       solo precione Enter para guardar en el archivo actual{fileName},
       o ingrese un nuevo archivo,
       o responda con / para cancelar el guardado.:  '''
    ans = raw_input(Guardararbol.__doc__.format(**locals())).strip()
    if ans and ans in '/\\':
        print('No fue guardado.')
    else:
        if ans:
            fileName = ans
        strToFile(Buscar(arbol), fileName) 
        print('Archivo', fileName, 'Guardado.')    

      
def fileToStr(fileName): 
    """Retorna la cadena que contiene el nombre del archivo."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

def strToFile(text, filename):
    """Escribe el archivo con el nombre que se dio."""
    output = open(filename,"w")
    output.write(text)
    output.close()

'''
if __name__ == '__main__':
	main()
'''