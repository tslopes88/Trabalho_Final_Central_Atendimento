# Central de Atendimento — Trabalho Final

Uma equipe recebe pedidos de suporte ao longo do dia: quem chegou primeiro deve ser atendido primeiro, e um atendimento feito por engano precisa poder ser desfeito. Este projeto representa esse fluxo em um programa de terminal.

O menu permite cadastrar chamados, atender pela ordem de chegada, desfazer o atendimento mais recente, organizar os pendentes por prioridade, procurar um protocolo e consultar um relatório. No desenvolvimento foram praticados fila (**FIFO**), pilha (**LIFO**), ordenação manual, busca binária e recursão.

## Executar pelo navegador

O projeto pode ser executado no GitHub Codespaces, sem instalar Python no computador:

1. Abra [este trabalho no Codespaces](https://codespaces.new/tslopes88/Trabalho_Final_Central_Atendimento) e entre na sua conta GitHub.
2. Crie um Codespace usando a branch `main` e aguarde o editor abrir.
3. Abra o terminal integrado pelo menu **Terminal → New Terminal**.
4. Execute o programa:

   ```bash
   python3 desafio_final.py
   ```

5. Digite o número de uma opção do menu e pressione Enter. Para encerrar, escolha `0`.

## Conferir os testes

No mesmo terminal, execute primeiro os testes do enunciado:

```bash
python3 desafio_final_testes.py
```

O resultado esperado é **9/9 testes passaram**. Para conferir também casos de borda e validações:

```bash
python3 desafio_final_testes_complementares.py
```

O resultado esperado é **11/11 testes complementares passaram**.

## Arquivos

- `desafio_final.py` — menu e funções que implementam as operações do trabalho.
- `desafio_final_testes.py` — os testes fornecidos com o enunciado.
- `desafio_final_testes_complementares.py` — testes adicionais para casos de borda.

Os chamados são exemplos de estudo e ficam na memória somente enquanto o programa está aberto. O Codespaces tem franquia mensal para contas pessoais; consulte [os limites e detalhes de cobrança](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces).
