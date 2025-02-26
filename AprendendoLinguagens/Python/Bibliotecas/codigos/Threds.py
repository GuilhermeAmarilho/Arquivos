import time
import threading
from concurrent.futures import ThreadPoolExecutor

# Single thread

def funcao_Recursiva_Single_Thread(count, max_count):
    if count >= max_count:
        return
    time.sleep(0.1)  # pausa de 0,1 segundo
    print(str(count + 1) + " execuções")
    funcao_Recursiva_Single_Thread(count + 1, max_count)

def programa_Com_Single_Thread(milisegundos):
    funcao_Recursiva_Single_Thread(0, milisegundos)

# Multi thread
# Cria e inicia 5 threads, cada uma executando a função recursiva

def funcao_Recursiva_Multi_Thread(name, count, max_count):
    if count >= max_count:
        print(f"{name} finalizado.")
        return
    time.sleep(0.1)
    funcao_Recursiva_Multi_Thread(name, count + 1, max_count)

def programa_Com_Multi_Thread(limite):
    threads = []
    start = time.time()
    for i in range(5):
        t = threading.Thread(
            target = funcao_Recursiva_Multi_Thread,
            args = (
                f"Thread-{i+1}",
                0,
                limite
            )
        )
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end = time.time()
    print("Tempo de execução (multithread): {:.2f} segundos".format(end - start))

# Outro método para manter a ordem em multithread é com o ThreadPoolExecutor

def metodo_Thread_Pool_Executor(name, steps):
    if steps <= 0:
        print(f"{name} finalizado.")
        return
    time.sleep(0.1)
    metodo_Thread_Pool_Executor(name, steps - 1)

def programa_Usando_Thread_Pool_Executor(limite):
    start = time.time()
    # Cria um ThreadPoolExecutor com 5 workers
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Submete 5 tarefas que executam n passos cada
        futures = [
            executor.submit(
                metodo_Thread_Pool_Executor,
                f"Thread-{i+1}",
                limite
            ) 
            for i in range(5)
        ]
        # Opcional: você pode iterar sobre os futures para obter resultados se necessário,
        # mas o gerenciador de contexto aguarda a conclusão de todas as tarefas.
    end = time.time()
    print("Tempo de execução (ThreadPoolExecutor): {:.2f} segundos".format(end - start))

# Usando MultiThread para executar uma função que demoraria 5 segundos em 1 segundo

def metodo_Recursivo_Para_Multi_Thread(name, steps):
    """
    Função recursiva que executa 'steps' iterações, 
    cada uma com um sleep de 0.1 segundo.
    """
    if steps <= 0:
        print(f"{name} finalizado.")
        return
    time.sleep(0.1)
    metodo_Recursivo_Para_Multi_Thread(name, steps - 1)

def programa_Usando_Multi_Thread(qt_Threads, tamanho):
    threads = []
    start = time.time()
    # Cria n threads, cada uma executando m passos recursivos
    for i in range(qt_Threads):
        t = threading.Thread(
            target = metodo_Recursivo_Para_Multi_Thread,
            args = (
                f"Thread-{i+1}",
                tamanho
            )
        )
        t.start()
        threads.append(t)
    # Aguarda todas as threads terminarem
    for t in threads:
        t.join()
    end = time.time()
    print("Tempo de execução (multithread): {:.2f} segundos".format(end - start))
