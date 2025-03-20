import time
from multiprocessing import Pool, cpu_count


def tarefa_pesada_Simples(n):
    total = 0
    # Loop para simular processamento intensivo
    for i in range(10_000_000):
        total += i * n
    return total

def programa_Sem_Multiprocessing():
    tarefas = list(range(1, 16))  # 8 tarefas (n de 1 a 8)
    resultados = []
    inicio = time.time()

    for n in tarefas:
        resultados.append(tarefa_pesada_Simples(n))

    fim = time.time()
    print("Resultados:", resultados)
    print("Tempo de execução (sequencial): {:.2f} segundos".format(fim - inicio))

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

# programa_Sem_Multiprocessing()
if __name__ == '__main__':
    # Por exemplo, utilizando 4 processos:
    # programa_Com_Multiprocessing(16
    print(f"Número de núcleos {cpu_count()}:")
