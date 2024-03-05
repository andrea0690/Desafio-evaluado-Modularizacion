def choose_level(n_pregunta, p_level):
    # Construir lógica para escoger el nivel
    ##################################################
    # Verificar que el número de pregunta sea válido
    if n_pregunta < 1 or n_pregunta > p_level * 3:
        return "Número de pregunta inválido"

    # Determinar el nivel de dificultad
    if p_level == 1:
        if n_pregunta <= 2:
            level = "básicas"
        elif n_pregunta <= 4:
            level = "intermedias"
        else:
            level = "avanzadas"
    elif p_level == 2:
        if n_pregunta % 2 == 0:
            level = "básicas"
        elif (n_pregunta // 2) % 2 == 1:
            level = "intermedias"
        else:
            level = "avanzadas"
    elif p_level == 3:
        if n_pregunta <= 3:
            level = "básicas"
        elif n_pregunta <= 6:
            level = "intermedias"
        else:
            level = "avanzadas"
    else:
        return "Número de preguntas por nivel inválido"

    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias