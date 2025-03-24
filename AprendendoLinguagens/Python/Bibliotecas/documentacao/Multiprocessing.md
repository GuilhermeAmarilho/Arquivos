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
- Overhead:
    - A criação de processos é mais custosa em termos de tempo e memória se comparada à criação de threads. Assim, é importante usar multiprocessing para tarefas que realmente se beneficiem do paralelismo, como cálculos intensivos ou processamento pesado.
### Pool VS Process:
- #### Controle vs. Abstração:
    - Usar Process oferece controle total sobre cada processo, enquanto o Pool abstrai a criação e o gerenciamento dos processos, distribuindo as tarefas de forma automática.
- #### Cenário de Uso:
    - Process: 
        - Melhor para tarefas distintas ou quando você precisa de um controle fino sobre cada processo.
    
    - Pool: 
        - Ideal para executar um grande número de tarefas semelhantes, como aplicar uma função a uma lista de itens.
    - A escolha entre os dois métodos depende do contexto da sua aplicação e do tipo de tarefas que você precisa executar em paralelo.

### Exemplo prático
- [Acesse o código base](../codigos/Multiprocessing.py)