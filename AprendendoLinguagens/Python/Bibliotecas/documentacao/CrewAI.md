# Python Com CrewAI

## Instalando os pacotes necessários para aplicação
> pip install crewai-tools
``` 
    Para rodar de forma manual, porém, é mais trabalhoso usando o pip, outro método é usando o uv.
```

## Instalando os pacotes com o UV
- Ele cria uma virtualenv para manter as versões dos packages inalterados.
1. Baixar o UV
    > powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
2. Instalando o CrewAI
    > uv tool install crewai
3. Criando a estrutura do projeto
    > crewai create crew <nome>
4. Rodando o crewai
    > crewai run
- Vai ser necessário informar a LLM e a API_KEY

A documentação e fundamental para essa biblioteca, o potencial dela é absurdo!

- [Instalação do CrewAI](https://docs.crewai.com/installation)
- [Primeiros passos](https://docs.crewai.com/quickstart)
- [Usando o arquivo .yaml para as tasks](https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended)
- [Usando o arquivo .yaml para os agentes](https://docs.crewai.com/concepts/agents#yaml-configuration-recommended)

---

## Estrutura base de um código CrewAi

```
    crewai_teste/
    ├── knowledge/
    │ └── user_preference.txt 
        # Preferências do usuário
    │ ├── src/
    │ └── teste/
    │ ├── init.py
        # Define o pacote Python
    │ ├── crew.py
        # Configuração da Crew
    │ ├── main.py
        # Ponto de entrada do projeto
    │ ├── config/
        # Arquivos de configuração
    │ └── tools/
        # Ferramentas personalizadas
    │ ├── tests/
    │ └── test_crew.py
        # Teste simples para execução da crew
    │ ├── .env
        # Variáveis de ambiente (API Keys, configs)
    ├── .gitignore
        # Ignora arquivos como .venv, pycache, etc.
    ├── pyproject.toml
        # Gerenciador de dependências (usando uv)
    └── README.md # Este arquivo
```

---

## O que faz cada parte do código mais complexos
- Agents.yaml
    - Esses agentes são as "personalidades" ou "papéis" que executam as tarefas. Aqui você especifica:
        - name: Nome do agente
        - role: Função do agente no sistema
        - goal: O que ele precisa alcançar
        - backstory: Contexto ou motivação do agente
        - tools: Quais ferramentas ele pode usa
- Tasks.yaml
    - Essas tarefas são as atividades a serem realizadas pelos agentes.
        - description: O que precisa ser feito
        - agent: Quem irá executar
        - expected_output: Resultado esperado
        - context: Tarefas anteriores que essa depende
- Tools,py
    - Por exemplo:
        ```python
        from crewai_tools import BaseTool
        class ReverterTextoTool(BaseTool):
            name = "reverter_texto"
            description = "Inverte a ordem dos caracteres de uma string."
            def _run(self, text: str) -> str:
                return text[::-1]
        ```
    - O tools é uma ferramenta que os agentes irão utilizar.
- Crew,py
    - Por exemplo:
        ```python
        from crewai import Agent, Crew, Process, Task
        from crewai.project import CrewBase, agent, crew, task
        
        @CrewBase
        class Teste():
        # Pega as regras dos agentes e tarefas
        agents_config = 'config/agents.yaml'
        tasks_config = 'config/tasks.yaml'
        # Exemplo de agentes de entrada 
        @agent
        def researcher(self) -> Agent:
            return Agent(
                config=self.agents_config['researcher'],
                verbose=True
            )
        @agent
        def reporting_analyst(self) -> Agent:
            return Agent(
                config=self.agents_config['reporting_analyst'],
                verbose=True
            )
        # Exemplos de agentes de saída
        @task
        def research_task(self) -> Task:
            return Task(
                config=self.tasks_config['research_task'],
            )
        @task
        def reporting_task(self) -> Task:
            return Task(
                config=self.tasks_config['reporting_task'],
                output_file='report.md'
            )
        # Regras de como a tripulação (crew) vai trabalhar.
        @crew
        def crew(self) -> Crew:
            return Crew(
                agents=self.agents,
                tasks=self.tasks,
                process=Process.sequential,
                verbose=True,
            )
        ```
- main,py
    - Por exemplo:
        ```python
        from <pasta>.crew import CrewItec
        def run():
            inputs = {
                'topic': '<tópico escolhido>'
            }    
            try:
                # Chama a tripulação passando o que for necessário
                <pasta>().crew().kickoff(inputs=inputs)        
            except:
                pass
        ```