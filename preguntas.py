preguntas_basicas = {
    'pregunta_1': {
        'enunciado':['Enunciado básico 1'],
        'alternativas': [
            ['alt_1', 0], 
            ['alt_2', 1], 
            ['alt_3', 0], 
            ['alt_4', 0]
        ]
    },
    'pregunta_2': {
        'enunciado':['Enunciado básico 2'],
        'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_3': {
        'enunciado':['Enunciado básico 3'],
        'alternativas': [['alt_1', 0], 
                        ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado':['Enunciado intermedio 1'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado intermedio 2'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    
'pregunta_3': {'enunciado':['Enunciado intermedio 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {
        'enunciado':['Enunciado avanzado 1'],
        'alternativas': [
            ['alt_1', 0], 
            ['alt_2', 1], 
            ['alt_3', 0], 
            ['alt_4', 0]
        ]
    },
    'pregunta_2': {'enunciado':['Enunciado avanzado 2'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_3': {'enunciado':['Enunciado avanzado 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

pool_preguntas = {
    'basicas': preguntas_basicas,
    'intermedias': preguntas_intermedias,
    'avanzadas': preguntas_avanzadas
}
if __name__ == '__main__':
    # print(pool_preguntas['basicas']['pregunta_2']['alternativas'][2])
    # print(pool_preguntas['basicas']['pregunta_1']['enunciado'][0])
    
    for k,v in pool_preguntas.items():
        print(k,v)
        # print(k,, json.dumps(v,sort_keys=True, indent=2))
        for k1,v1 in v.items():
            print(k1,v1['enunciado'][0])
            print('____________________')
        