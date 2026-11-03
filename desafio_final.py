"""
DESAFIO FINAL - Central de Atendimento
Aluno: Thiago da Silva Lopes - ADS

Programa de atendimento de chamados feito para o trabalho final.
Para executar: python desafio_final.py
Para rodar os testes: python desafio_final_testes.py
"""

from collections import deque


# ---------------------------------------------------------------
# NIVEL 1 - FILA: abrir e atender chamados
# ---------------------------------------------------------------
def criar_chamado(protocolo, nome, descricao, prioridade):
    """Ja pronta: cada chamado e um dicionario."""
    return {
        "protocolo": protocolo,
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,      # 1 = baixa, 2 = media, 3 = alta
        "status": "pendente",
    }


def abrir_chamado(fila, todos, nome, descricao, prioridade):
    """Cria um chamado e o coloca no fim da fila."""
    if not isinstance(nome, str) or not nome.strip():
        raise ValueError("Nome do chamado deve ser informado.")
    if not isinstance(descricao, str) or not descricao.strip():
        raise ValueError("Descricao do chamado deve ser informada.")
    if isinstance(prioridade, bool) or not isinstance(prioridade, int) or prioridade not in (1, 2, 3):
        raise ValueError("Prioridade deve ser 1, 2 ou 3.")

    protocolo = len(todos) + 1
    chamado = criar_chamado(protocolo, nome, descricao, prioridade)
    fila.append(chamado)
    todos.append(chamado)
    return chamado


def atender_proximo(fila, historico):
    """Atende o primeiro chamado pendente e registra o atendimento."""
    if not fila:
        return None

    chamado = fila.popleft()
    chamado["status"] = "atendido"
    historico.append(chamado)
    return chamado


# ---------------------------------------------------------------
# NIVEL 2 - PILHA: desfazer o ultimo atendimento
# ---------------------------------------------------------------
def desfazer_atendimento(fila, historico):
    """Desfaz o atendimento mais recente e devolve o chamado à fila."""
    if not historico:
        return None

    chamado = historico.pop()
    chamado["status"] = "pendente"
    fila.appendleft(chamado)
    return chamado


# ---------------------------------------------------------------
# NIVEL 3 - ORDENACAO: lista de pendentes por prioridade
# ---------------------------------------------------------------
def ordenar_por_prioridade(chamados):
    """Retorna uma nova lista de chamados ordenada por prioridade."""
    ordenados = list(chamados)

    for fim in range(len(ordenados) - 1, 0, -1):
        trocou = False
        for indice in range(fim):
            if ordenados[indice]["prioridade"] < ordenados[indice + 1]["prioridade"]:
                ordenados[indice], ordenados[indice + 1] = (
                    ordenados[indice + 1],
                    ordenados[indice],
                )
                trocou = True
        if not trocou:
            break

    return ordenados


# ---------------------------------------------------------------
# NIVEL 4 - BUSCA BINARIA e RECURSAO
# ---------------------------------------------------------------
def buscar_protocolo(todos, protocolo):
    """Procura um protocolo na lista de chamados."""
    inicio = 0
    fim = len(todos) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        protocolo_atual = todos[meio]["protocolo"]

        if protocolo_atual == protocolo:
            return todos[meio]
        if protocolo_atual < protocolo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None


def contar_por_prioridade(chamados, prioridade, i=0):
    """Conta recursivamente os chamados com a prioridade informada."""
    if i >= len(chamados):
        return 0

    atual = 1 if chamados[i]["prioridade"] == prioridade else 0
    return atual + contar_por_prioridade(chamados, prioridade, i + 1)


# ---------------------------------------------------------------
# INTERFACE (menu)
# ---------------------------------------------------------------
def ler_inteiro(mensagem, minimo, maximo):
    while True:
        texto = input(mensagem)
        if texto.isdigit() and minimo <= int(texto) <= maximo:
            return int(texto)
        print(f"Digite um numero entre {minimo} e {maximo}.")


def mostrar(chamado):
    print(f"#{chamado['protocolo']:03d} | prioridade {chamado['prioridade']} | "
          f"{chamado['nome']}: {chamado['descricao']} [{chamado['status']}]")


def mostrar_guia():
    print("\n=== GUIA DE USO ===")
    print("1) Abrir chamado: informe nome, descricao e prioridade.")
    print("   Prioridades: 1 = baixa, 2 = media, 3 = alta.")
    print("   O sistema cria um protocolo e inicia o chamado como pendente.")
    print("2) Atender proximo: atende o chamado pendente mais antigo (FIFO).")
    print("3) Desfazer ultimo atendimento: devolve o ultimo atendido ao")
    print("   inicio da fila. Ele sera o proximo a ser atendido (LIFO).")
    print("4) Listar pendentes: mostra os chamados pendentes por prioridade,")
    print("   da mais alta para a mais baixa. A fila de atendimento nao muda.")
    print("5) Buscar por protocolo: digite o numero recebido ao abrir o chamado.")
    print("6) Relatorio: mostra totais e a quantidade por prioridade.")
    print("   As quantidades por prioridade incluem todos os chamados abertos.")
    print("Use 7 para consultar este guia novamente e 0 para sair.")
    print("Os dados ficam apenas na memoria e sao apagados ao encerrar o programa.")


def menu():
    fila, todos, historico = deque(), [], []
    while True:
        print("\n=== CENTRAL DE ATENDIMENTO ===")
        print("1) Abrir chamado")
        print("2) Atender proximo")
        print("3) Desfazer ultimo atendimento")
        print("4) Listar pendentes por prioridade")
        print("5) Buscar por protocolo")
        print("6) Relatorio")
        print("7) Guia de uso")
        print("0) Sair")
        op = ler_inteiro("Escolha: ", 0, 7)

        if op == 0:
            print("Ate a proxima!")
            break
        elif op == 1:
            nome = input("Nome: ")
            desc = input("Descricao: ")
            prio = ler_inteiro("Prioridade (1=baixa, 2=media, 3=alta): ", 1, 3)
            try:
                mostrar(abrir_chamado(fila, todos, nome, desc, prio))
            except ValueError as erro:
                print(f"Erro: {erro}")
        elif op == 2:
            c = atender_proximo(fila, historico)
            print("Atendendo:" if c else "Fila vazia.")
            if c:
                mostrar(c)
        elif op == 3:
            c = desfazer_atendimento(fila, historico)
            print("Devolvido a fila:" if c else "Nada para desfazer.")
            if c:
                mostrar(c)
        elif op == 4:
            pendentes = ordenar_por_prioridade(fila)
            if not pendentes:
                print("Nenhum chamado pendente.")
            for c in pendentes:
                mostrar(c)
        elif op == 5:
            p = ler_inteiro("Protocolo: ", 1, 10**6)
            c = buscar_protocolo(todos, p)
            mostrar(c) if c else print("Protocolo nao encontrado.")
        elif op == 6:
            print(f"Total aberto: {len(todos)} | Pendentes: {len(fila)} | "
                  f"Atendidos: {len(historico)}")
            for p in (3, 2, 1):
                print(f"Prioridade {p}: {contar_por_prioridade(todos, p)}")
        elif op == 7:
            mostrar_guia()


if __name__ == "__main__":
    menu()
