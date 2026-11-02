# Central de Atendimento

Trabalho final de Python que simula o atendimento de chamados em uma equipe de suporte. O programa permite cadastrar solicitações, atender pela ordem de chegada e acompanhar os chamados pelo terminal.

## Sobre o projeto

O exercício reúne estruturas de dados e algoritmos estudados durante a disciplina. Os chamados ficam na memória enquanto o programa está aberto; não há banco de dados nem salvamento permanente.

## Funcionalidades

- Cadastrar chamados com nome, descrição e prioridade.
- Atender o próximo chamado pela ordem de chegada.
- Desfazer o atendimento mais recente e devolver o chamado ao início da fila.
- Listar os chamados pendentes por prioridade.
- Buscar um chamado pelo protocolo.
- Consultar o total de chamados e a contagem por prioridade.

## Exemplo de execução

Este trecho resume uma execução do programa. Os menus repetidos entre as operações foram omitidos para facilitar a leitura.

```text
=== CENTRAL DE ATENDIMENTO ===
1) Abrir chamado
2) Atender proximo
3) Desfazer ultimo atendimento
4) Listar pendentes por prioridade
5) Buscar por protocolo
6) Relatorio
0) Sair
Escolha: 1
Nome: Ana
Descricao: Internet instavel
Prioridade (1-3): 3
#001 | prioridade 3 | Ana: Internet instavel [pendente]

Escolha: 2
Atendendo:
#001 | prioridade 3 | Ana: Internet instavel [atendido]

Escolha: 6
Total aberto: 1 | Pendentes: 0 | Atendidos: 1
Prioridade 3: 1
Prioridade 2: 0
Prioridade 1: 0

Escolha: 0
Ate a proxima!
```

## Conceitos praticados

- Fila (**FIFO**) para atender os chamados na ordem de chegada.
- Pilha (**LIFO**) para desfazer o atendimento mais recente.
- Bubble Sort para organizar chamados por prioridade, mantendo a ordem entre prioridades iguais.
- Busca binária por protocolo.
- Recursividade para contar chamados por prioridade.

## Executar pelo navegador

O projeto pode ser executado no GitHub Codespaces, sem instalar Python no computador:

1. Abra [este trabalho no Codespaces](https://codespaces.new/tslopes88/Trabalho_Final_Central_Atendimento) e entre na sua conta GitHub.
2. Crie um Codespace usando a branch `main` e aguarde o editor abrir.
3. Abra o terminal integrado pelo menu **Terminal → New Terminal**.
4. Execute:

   ```bash
   python3 desafio_final.py
   ```

5. Escolha uma opção do menu. Para encerrar, digite `0`.

## Executar os testes

Os testes do enunciado:

```bash
python3 desafio_final_testes.py
```

Os testes complementares, que verificam também casos de borda e entradas inválidas:

```bash
python3 desafio_final_testes_complementares.py
```

## Arquivos

- `desafio_final.py` — menu e funções do programa.
- `desafio_final_testes.py` — testes fornecidos com o enunciado.
- `desafio_final_testes_complementares.py` — testes adicionais.

O Codespaces tem franquia mensal para contas pessoais. Consulte [os limites e detalhes de cobrança](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces).
