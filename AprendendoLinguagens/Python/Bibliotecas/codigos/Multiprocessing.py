import time
from multiprocessing import Pool, cpu_count, Queue, Process

# Usando um único núcleo de processamento
def tarefa_pesada_Simples(n):
    total = 0
    # Loop para simular processamento intensivo
    for i in range(10_000_000):
        total += i * n
    return total
def programa_Sem_Multiprocessing():
    tarefas = list(range(1, 9))
    resultados = []
    inicio = time.time()

    for n in tarefas:
        resultados.append(tarefa_pesada_Simples(n))

    fim = time.time()
    print("Resultados:", resultados)
    print("Tempo de execução (sequencial): {:.2f} segundos".format(fim - inicio))

# Método usando diversos núcleos de processamento simultâneo
# É bom para quando há diversos processos independentes, não necessitando seguir uma ordem lógica prévia
# É o método POOL
def tarefa_pesada_Com_Multiprocessamento(n):
    total = 0
    # Loop para simular processamento intensivo
    for i in range(10_000_000):
        total += i * n
    return total
def programa_Com_Multiprocessing(nucleos):
    tarefas = list(range(1, 16))  # 8 tarefas (n de 1 a 8)
    inicio = time.time()   
    # Cria um pool de processos. Ajuste "processes" conforme o número de núcleos disponíveis.
    with Pool(processes = nucleos) as pool:
        resultados = pool.map(tarefa_pesada_Com_Multiprocessamento, tarefas)
    fim = time.time()
    print("Resultados:", resultados)
    print("Tempo de execução (multiprocessing): {:.2f} segundos".format(fim - inicio))

# Pool vs Process
# Problemática: Para cada número em uma lista, calcularemos uma soma que fará ter CPU-Bound. A função fará um loop * 10^6 (10KK), acumulando um valor cumulativo. Com isso, vamos refazer, usando POOL e PROCESS.

def programa_Com_Pool():
    start = time.time()
    tasks = [1, 2, 3, 4, 5, 6, 7, 8] # Ex de 8 tarefas
    with Pool(
        processes = 8
    ) as pool:
        results = pool.map(tarefa_pesada_Simples, tasks)
    
    end = time.time()
    print("Pool - Resultados:", results)
    print("Pool - Tempo de execução: {:.2f} segundos".format(end - start))

def tarefa_Pesada_Process(n, output):
    total = 0
    # Loop para simular processamento intenso
    for i in range(1, 10_000_000):
        total += i * n
    output.put((n, total))

def programa_Com_Process():
    start = time.time()
    tasks = [1, 2, 3, 4, 5, 6, 7, 8]
    processes = []
    output = Queue()
    # Cria um processo p cada tarefa e começa
    for n in tasks:
        p = Process(
            target = tarefa_Pesada_Process,
            args = (
                n, 
                output
            )
        )
        p.start()
        processes.append(p)
    
    # espera terminar tds processos
    for p in processes:
        p.join()
    
    # Pega os resultados do Queue
    results = []
    while not output.empty():
        results.append(output.get())
    
    
    end = time.time()
    print("Process - Resultados:", [res[1] for res in results])
    print("Process - Tempo de execução: {:.2f} segundos".format(end - start))


if __name__ == '__main__':
    print('\n Programa sem multiprocessamento\n')
    programa_Sem_Multiprocessing()
    print('\n\n Programa com multiprocessamento em Pool\n')
    programa_Com_Pool()
    print('\n\n Programa com multiprocessamento em Process\n')
    programa_Com_Process()
    