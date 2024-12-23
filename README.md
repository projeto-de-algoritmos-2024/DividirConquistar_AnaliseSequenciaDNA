
# Análise de Sequência Biológica

**Número da Lista**: 25  
**Conteúdo da Disciplina**: Dividir e Conquistar  

## Alunos

| Matrícula  | Aluno                                 |
|------------|---------------------------------------|
| 21/1030700 | Chaydson Ferreira da Aparecida        |
| 21/1030676 | Ana Luíza Rodrigues da Silva          |

## Sobre o Projeto

Este projeto implementa uma análise de sequências biológicas, utilizando o algoritmo de **Merge Sort** para calcular o grau de desordem em uma sequência de DNA/RNA. A aplicação conta com uma interface gráfica interativa que permite visualizar o processo de ordenação e o cálculo do número de inversões, que é utilizado para determinar o índice de desordem da sequência.

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Como Rodar o Projeto

### 1. Clone o repositório

Clone o repositório em seu ambiente local:

```bash
git clone git@github.com:projeto-de-algoritmos-2024/DividirConquistar_AnaliseSequenciaDNA.git
cd DividirConquistar_AnaliseSequenciaDNA
```

### 2. Crie e ative um ambiente virtual (recomendado)

Crie um ambiente virtual para garantir que as dependências sejam isoladas:

```bash
python -m venv venv
```

#### No Windows

```bash
venv\Scripts\activate
```

#### No Linux/MacOS

```bash
source venv/bin/activate
```

### 3. Instale as dependências

Instale as bibliotecas necessárias, listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Execute o programa

Para iniciar o programa, execute o seguinte comando:

```bash
python main.py
```

### 5. Como Usar o Programa

1. Ao executar o programa, uma janela será aberta solicitando a entrada de uma sequência biológica.
2. Insira uma sequência válida de DNA/RNA, utilizando apenas os caracteres **A**, **C**, **G**, **T**, **U** (para RNA).
3. Clique no botão "Enviar" ou pressione **Enter**.
4. Observe a visualização do processo de ordenação das sequências.
5. Ao final, o programa exibirá o número de inversões realizadas e o índice de desordem da sequência.
