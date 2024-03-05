
def validate(opciones, eleccion):
   
    print(eleccion,opciones)
    
    if eleccion in opciones:
        return eleccion
    else:
        return 'Opción no válida, ingrese una de las opciones válidas: '    

if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    # numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    resultado=validate(letras, eleccion)
    
    print(resultado)
    
    
