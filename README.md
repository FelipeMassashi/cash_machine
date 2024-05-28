# Caixa Eletrônico em Python

Este é um projeto de simulação de um caixa eletrônico simples escrito em Python. Ele permite que os usuários realizem operações bancárias básicas, como consultar saldo, sacar dinheiro, depositar dinheiro, ver extrato e transferir dinheiro entre contas. O código também implementa uma verificação de senha para acessar as funcionalidades do caixa eletrônico.

## Funcionalidades

- **Consultar Saldo:** Permite ao usuário verificar o saldo disponível na conta.
- **Sacar Dinheiro:** Permite ao usuário sacar um valor especificado do saldo disponível, se houver fundos suficientes.
- **Depositar Dinheiro:** Permite ao usuário depositar um valor especificado na conta.
- **Ver Extrato:** Mostra todas as operações realizadas na conta (saques e depósitos).
- **Transferir Dinheiro:** Permite ao usuário transferir dinheiro da conta principal para uma conta poupança.
- **Verificação de Senha:** Solicita ao usuário criar e verificar uma senha para acessar o caixa eletrônico.

## Requisitos

- Python 3.6 ou superior
- Biblioteca `locale` (já incluída na biblioteca padrão do Python)

## Como Rodar o Código

1. **Clone o Repositório:**
    ```bash
    git clone https://github.com/seu-usuario/caixa-eletronico.git
    cd caixa-eletronico
    ```

2. **Execute o Script:**
    ```bash
    python main.py
    ```

3. **Siga as Instruções no Terminal:**
    - Crie uma senha para acessar o caixa eletrônico.
    - Use essa senha para realizar operações bancárias.
    - Utilize o menu interativo para navegar pelas opções disponíveis.

## Exemplo de Uso

1. Ao rodar o script, você será solicitado a criar uma senha:
    ```
    Crie uma senha para acessar o caixa eletrônico: ******
    ```

2. Digite a senha criada para acessar as funcionalidades:
    ```
    Digite a senha: ******
    ```

3. Após a verificação da senha, você verá o menu principal:
    ```
    === Caixa Eletrônico ===

    1. Consultar Saldo
    2. Sacar Dinheiro
    3. Depositar Dinheiro
    4. Ver Extrato
    5. Transferir Dinheiro
    6. Sair

    Escolha uma opção:
    ```

4. Escolha a opção desejada e siga as instruções na tela.

## Detalhes Técnicos

- **Classe `CaixaEletronico`:**
    - `__init__(self, saldo_inicial=0)`: Inicializa a classe com um saldo inicial e um extrato vazio.
    - `consultar_saldo(self)`: Retorna o saldo atual.
    - `sacar_dinheiro(self, valor)`: Deduz o valor do saldo se houver fundos suficientes e adiciona a operação ao extrato.
    - `depositar_dinheiro(self, valor)`: Adiciona o valor ao saldo e registra a operação no extrato.
    - `ver_extrato(self)`: Retorna o extrato das operações.
    - `transferir(self, outro_caixa, valor)`: Transfere um valor especificado para outra conta se houver saldo suficiente.

- **Funções Auxiliares:**
    - `criar_senha()`: Solicita ao usuário criar uma senha.
    - `solicitar_senha()`: Solicita ao usuário verificar a senha antes de acessar o caixa eletrônico.
    - `obter_valor_monetario(mensagem)`: Solicita ao usuário inserir um valor monetário válido e trata entradas inválidas.

## O Projeto como um Autômato

Este projeto pode ser considerado um tipo de autômato, especificamente um autômato finito determinístico (DFA - Deterministic Finite Automaton). 

### O que é um Autômato?

Um autômato é um modelo matemático para uma máquina abstrata que pode estar em um de um número finito de estados a qualquer momento. Ele lê uma string de símbolos (entrada) e muda de estado de acordo com uma função de transição.

### Por que este projeto é um Autômato?

1. **Estados Finitos:**
    - O caixa eletrônico pode estar em diferentes estados, como:
        - Espera pela senha do usuário.
        - Menu principal.
        - Processamento de saque.
        - Processamento de depósito.
        - Processamento de transferência.
        - Exibição de saldo e extrato.
        
2. **Transições Determinísticas:**
    - O comportamento do caixa eletrônico é determinístico, o que significa que para cada estado e entrada, há uma transição bem definida para um próximo estado. Por exemplo:
        - Após a verificação da senha, o sistema transita para o estado de exibir o menu principal.
        - Ao escolher uma opção no menu, o sistema transita para o estado correspondente à operação escolhida.

3. **Função de Transição:**
    - As transições entre estados são implementadas pelo menu interativo, onde cada escolha do usuário (entrada) determina a próxima operação (estado).


