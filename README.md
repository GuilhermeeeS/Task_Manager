# Gerenciador de Tarefas 
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height=50/>
          

Este repositório contém um sistema de gerenciamento de tarefas simples, desenvolvido em Python. 
Ele permite criar, listar, concluir, remover e filtrar tarefas. As tarefas são armazenadas em um arquivo JSON, garantindo persistência entre execuções do programa.

# Funcionalidades
- Adicionar tarefas com descrição, prazo e prioridade.
- Listar tarefas pendentes ou concluídas.
- Marcar tarefas como concluídas.
- Remover tarefas.
- Filtrar tarefas pendentes por prioridade.
- Armazenamento das tarefas em um arquivo JSON (```tasks.json```)

# Estrutura do Projeto
O projeto é dividido em dois arquivos:

- ```main.py```: Gerencia a interface do usuário, exibindo o menu e capturando as entradas.
- ```tasks.py```: Contém a classe ```TaskManager```, responsável pela lógica de manipulação das tarefas.

## Personalização
- Para alterar o nome ou o caminho do arquivo de armazenamento (tasks.json), modifique o parâmetro ```file_name``` na classe ```TaskManager``` em ```tasks.py```.
