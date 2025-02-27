# Python com Multiprocessamento
- Quando for usar diversos recursos da biblioteca de multiprocessamento
    > import multiprocessing
- Inicialmente, a sub-biblioteca pool será suficiente
    > from multiprocessing import Pool
## Conceito:
- Processos Independentes:
    - Ao contrário do multithreading, que utiliza threads dentro de um mesmo processo, a biblioteca multiprocessing cria processos separados. Cada processo tem seu próprio interpretador Python e espaço de memória, o que permite executar tarefas em paralelo sem as limitações do GIL (Global Interpreter Lock).
- Paralelismo Real:
    - Como cada processo roda em um núcleo diferente (ou pode ser distribuído em núcleos distintos), é possível aproveitar ao máximo as capacidades de máquinas com múltiplos núcleos, tornando-a ideal para tarefas que exigem muito processamento.
## Características:
- Contorno do GIL:
    - Por cada processo ter seu próprio interpretador, o GIL não restringe a execução paralela de tarefas CPU-bound, permitindo ganho de performance em cálculos intensivos.
- Isolamento de Memória:
    - Processos não compartilham memória por padrão. Isso melhora a segurança e estabilidade, mas exige mecanismos explícitos de comunicação se for necessário compartilhar dados (como Queue, Pipe ou Manager).
         > A biblioteca multiprocessing oferece diversas formas de comunicação e compartilhamento de dados entre processos. Entre elas, destacam-se o uso de Queue, Pipe e Manager. 
    - Queue




- Sincronização e Comunicação:
    - Assim como o módulo threading oferece locks, semáforos e outros mecanismos de sincronização, o multiprocessing fornece suas próprias versões adaptadas para processos, como Lock, Semaphore, Event e Barrier.
- 

### Exemplo prático
- [Acesse o código base](../codigos/Multiprocessing.py)