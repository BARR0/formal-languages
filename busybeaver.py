from joblib import Parallel, delayed
import multiprocessing

# Estado:
# {
#     valor_leido: (valor_escrito, direccion, siguiente_estado),
#     ...
# }

# estado -1 es terminar
# direccion 0 es izquierda
# direccion 1 es derecha

# Ejemplo maquina de 2 estados
TM2 = [
    {
        0: (1, 1, 1),
        1: (1, 0, 1)
    },
    {
        0: (1, 0, 0),
        1: (1, 1, -1)
    },
]

# Correr hasta el numero de pasos especificado
def run(tm, maxsteps):
    state = tm[0]
    tape = [0 for i in range(maxsteps * 2)]
    i = len(tape) // 2
    steps = 0
    while state[tape[i]][2] != -1:
        # print(tape, steps)
        action = state[tape[i]]
        tape[i] = action[0]
        if action[1] == 0:
            i -= 1
        else:
            i += 1
        state = tm[action[2]]
        steps += 1
        if steps >= maxsteps:
            return [-1]
    action = state[tape[i]]
    tape[i] = action[0]
    return tape

# Probar todas las MT de 2 estados
def testall2():
    maxtm = None
    sigma = 0
    allactions = [(a, b, c) for a in range(2)
                  for b in range(2) for c in range(-1, 2)]
    for i in allactions:
        for j in allactions:
            for k in allactions:
                for l in allactions:
                    tm = [
                        {
                            0: i,
                            1: j
                        },
                        {
                            0: k,
                            1: l
                        }
                    ]
                    # print(tm)
                    tmp = sum(run(tm, 6)) # Maximo numero de pasos a probar
                    if tmp > sigma:
                        sigma = tmp
                        maxtm = tm

    return maxtm, sigma

# Funcion de ayuda para implementacion paralela
def testall4_con(i):
    maxtm = None
    sigma = 0
    allactions = [(a, b, c) for a in range(2)
                  for b in range(2) for c in range(-1, 4)]
    print(len(allactions))

    for j in allactions:
        for k in allactions:
            for l in allactions:
                for m in allactions:
                    for n in allactions:
                        for o in allactions:
                            for p in allactions:
                                tm = [
                                    {
                                        0: i,
                                        1: j
                                    },
                                    {
                                        0: k,
                                        1: l
                                    },
                                    {
                                        0: m,
                                        1: n
                                    },
                                    {
                                        0: o,
                                        1: p
                                    },
                                ]
                                tmp = sum(run(tm, 107)) # Maximo numero de pasos a probar
                                # print(tm, tmp)
                                if tmp > sigma:
                                    print(tm, tmp)
                                    sigma = tmp
                                    maxtm = tm
            print('HIHIHI', k)
        print('HIHI', j)
    print('HI', i)

    return maxtm, sigma

# Funcion que prueba todas las MT de 4 estados de manera paralela
def getmaxcon():
    # what are your inputs, and what operation do you want to 
    # perform on each input. For example...
    inputs = [(a, b, c) for a in range(2)
                  for b in range(2) for c in range(-1, 4)]

    num_cores = multiprocessing.cpu_count()
        
    results = Parallel(n_jobs=num_cores)(delayed(testall4_con)(i) for i in inputs)
    return results

# Funcion que prueba todas las MT de 4 estados
def testall4():
    maxtm = None
    sigma = 0
    allactions = [(a, b, c) for a in range(2)
                  for b in range(2) for c in range(-1, 4)]
    allactions.reverse()
    print(len(allactions))

    for i in allactions:
        for j in allactions:
            for k in allactions:
                for l in allactions:
                    for m in allactions:
                        for n in allactions:
                            for o in allactions:
                                for p in allactions:
                                    tm = [
                                        {
                                            0: i,
                                            1: j
                                        },
                                        {
                                            0: k,
                                            1: l
                                        },
                                        {
                                            0: m,
                                            1: n
                                        },
                                        {
                                            0: o,
                                            1: p
                                        },
                                    ]
                                    tmp = sum(run(tm, 107)) # Maximo numero de pasos a probar
                                    # print(tm, tmp)
                                    if tmp > sigma:
                                        print(tm, tmp)
                                        sigma = tmp
                                        maxtm = tm
                print('HIHIHI', k)
            print('HIHI', j)
        print('HI', i)

    return maxtm, sigma

# Ejecutar prueba de 4 estados paralela
print(getmaxcon())
