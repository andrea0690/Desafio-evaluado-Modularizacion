import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    # usar opciones desde ambiente global
    global opciones
    
    #escoger preguntas por dificultad
    preguntas = opciones[dificultad]
    
    # escoger una pregunta
    n_elegido = random.choice(preguntas)
    # eliminarla del ambiente global para no escogerla de nuevo
    opts = [opt for opt in opciones[dificultad] if n_elegido != opt]
    opciones[dificultad] = opts
    
    # escoger enunciado y alternativas mezcladas
    pregunta = {}
    
    for key, value in p.pool_preguntas[dificultad].items():
        if str(n_elegido) in key:
            pregunta = value
            break

    alternativas = shuffle_alt(pregunta)
    
    return pregunta["enunciado"], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')