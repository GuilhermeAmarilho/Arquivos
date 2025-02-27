# Python com Thread

## Não é nescessário fazer a instalação, é nativo do python

- Uma thread é uma unidade de execução dentro de um processo. Threads compartilham a mesma memória e recursos do processo pai, permitindo a execução concorrente de várias tarefas.

### Concorrência vs. Paralelismo:

- Concorrência:
    - Permite que várias tarefas sejam intercaladas, ou seja, uma tarefa pode iniciar, pausar e depois retomar enquanto outra é executada.
- Paralelismo:
    - Execução simultânea de tarefas, normalmente em múltiplos núcleos de CPU.
- Threading:
    - A biblioteca padrão threading é a forma mais direta de criar e gerenciar threads em Python.
- Exemplo Básico:
    >>>
        import threading
        
        def tarefa(nome):
            print(f"Thread {nome} executando...")
        t = threading.Thread(target=tarefa, args=("A",))
        t.start()
        t.join()
### Sincronização e Controle de Concorrência:
    - Quando várias threads acessam ou modificam recursos compartilhados, podem ocorrer race conditions. Para evitar isso, usamos mecanismos de sincronização, como locks.
    >>>
        import threading

        contador = 0
        lock = threading.Lock()

        def incrementar():
            global contador
            for _ in range(100000):
                with lock:
                    contador += 1
        threads = [
            threading.Thread(target=incrementar) 
            for _ in range(10)
        ]

        for t in threads:
            t.start()
        for t in threads:
            t.join()

        print(contador)
    - O uso de lock (mutex) evita que duas threads atualizem o contador ao mesmo tempo, garantindo resultados corretos.

### Exemplo prático
- [Acesse o código base](../codigos/Threds.py)