
def validate(opciones, eleccion):
    
    if eleccion in opciones:
        return eleccion
    else:
        # mejora para solicitar opcion valida obligatoria
        while eleccion not in opciones:
            eleccion = input('Ingrese una de las opciones validas ' + ', '.join(opciones) + ': ')
        return eleccion    

if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    # numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    resultado=validate(letras, eleccion)
    
    print(resultado)
    
    
