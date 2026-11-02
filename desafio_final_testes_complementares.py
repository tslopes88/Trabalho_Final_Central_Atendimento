from collections import deque
import desafio_final as d


def testar(nome, func):
    try:
        func()
        print(f"[OK] {nome}")
        return True
    except Exception as erro:
        print(f"[FALHA] {nome}: {type(erro).__name__}: {erro}")
        return False


def teste_ordenacao_lista_vazia():
    assert d.ordenar_por_prioridade([]) == []


def teste_ordenacao_um_elemento():
    fila = deque([d.criar_chamado(1, "Ana", "desc", 2)])
    assert [c["nome"] for c in d.ordenar_por_prioridade(fila)] == ["Ana"]


def teste_ordenacao_prioridades_iguais():
    fila = deque([
        d.criar_chamado(1, "Ana", "desc", 2),
        d.criar_chamado(2, "Bruno", "desc", 2),
        d.criar_chamado(3, "Carla", "desc", 2),
    ])
    ordenados = d.ordenar_por_prioridade(fila)
    assert [c["nome"] for c in ordenados] == ["Ana", "Bruno", "Carla"]


def teste_preservacao_lista_original():
    fila = deque([
        d.criar_chamado(1, "Ana", "desc", 2),
        d.criar_chamado(2, "Bruno", "desc", 3),
    ])
    original = [c["nome"] for c in fila]
    d.ordenar_por_prioridade(fila)
    assert [c["nome"] for c in fila] == original


def teste_busca_lista_vazia():
    assert d.buscar_protocolo([], 1) is None


def teste_busca_protocolo_inexistente():
    todos = [d.criar_chamado(1, "Ana", "desc", 1), d.criar_chamado(2, "Bruno", "desc", 2)]
    assert d.buscar_protocolo(todos, 99) is None


def teste_busca_lista_maior():
    todos = [d.criar_chamado(i, f"Pessoa {i}", "desc", 1 + (i % 3)) for i in range(1, 11)]
    assert d.buscar_protocolo(todos, 7)["nome"] == "Pessoa 7"
    assert d.buscar_protocolo(todos, 10)["nome"] == "Pessoa 10"


def teste_varios_atendimentos_consecutivos():
    fila = deque()
    todos = []
    historico = []
    for nome in ["Ana", "Bruno", "Carla"]:
        d.abrir_chamado(fila, todos, nome, "desc", 2)
    assert [d.atender_proximo(fila, historico)["nome"] for _ in range(3)] == ["Ana", "Bruno", "Carla"]
    assert len(fila) == 0 and len(historico) == 3


def teste_varios_desfazimentos_consecutivos():
    fila = deque()
    todos = []
    historico = []
    for nome in ["Ana", "Bruno", "Carla"]:
        d.abrir_chamado(fila, todos, nome, "desc", 2)
    for _ in range(3):
        d.atender_proximo(fila, historico)
    for _ in range(3):
        chamado = d.desfazer_atendimento(fila, historico)
        assert chamado["status"] == "pendente"
    assert [c["nome"] for c in fila] == ["Ana", "Bruno", "Carla"]


def teste_consistencia_estados_apos_operacoes_sucessivas():
    fila = deque()
    todos = []
    historico = []
    d.abrir_chamado(fila, todos, "Ana", "desc", 1)
    d.abrir_chamado(fila, todos, "Bruno", "desc", 3)
    atendido = d.atender_proximo(fila, historico)
    assert atendido["nome"] == "Ana"
    d.abrir_chamado(fila, todos, "Carla", "desc", 2)
    assert [c["nome"] for c in fila] == ["Bruno", "Carla"]
    retornado = d.desfazer_atendimento(fila, historico)
    assert retornado["nome"] == "Ana"
    assert [c["nome"] for c in fila] == ["Ana", "Bruno", "Carla"]
    assert len(historico) == 0


def teste_abrir_chamado_dados_invalidos():
    fila = deque()
    todos = []
    try:
        d.abrir_chamado(fila, todos, "", "desc", 1)
        raise AssertionError("nome vazio deveria causar ValueError")
    except ValueError:
        pass

    try:
        d.abrir_chamado(fila, todos, "Ana", "", 2)
        raise AssertionError("descricao vazia deveria causar ValueError")
    except ValueError:
        pass

    try:
        d.abrir_chamado(fila, todos, "Ana", "desc", 0)
        raise AssertionError("prioridade invalida deveria causar ValueError")
    except ValueError:
        pass

    for prioridade in (True, "2", 4):
        try:
            d.abrir_chamado(fila, todos, "Ana", "desc", prioridade)
            raise AssertionError("prioridade de tipo ou valor invalido deveria causar ValueError")
        except ValueError:
            pass


casos = [
    ("lista vazia", teste_ordenacao_lista_vazia),
    ("um elemento", teste_ordenacao_um_elemento),
    ("prioridades iguais", teste_ordenacao_prioridades_iguais),
    ("preservacao da lista original", teste_preservacao_lista_original),
    ("busca em lista vazia", teste_busca_lista_vazia),
    ("busca por protocolo inexistente", teste_busca_protocolo_inexistente),
    ("busca em lista maior", teste_busca_lista_maior),
    ("vários atendimentos consecutivos", teste_varios_atendimentos_consecutivos),
    ("vários desfazimentos consecutivos", teste_varios_desfazimentos_consecutivos),
    ("consistencia apos operacoes sucessivas", teste_consistencia_estados_apos_operacoes_sucessivas),
    ("dados invalidos", teste_abrir_chamado_dados_invalidos),
]

resultados = [testar(nome, func) for nome, func in casos]
qtd = sum(resultados)
print(f"\nResultado: {qtd}/{len(resultados)} testes complementares passaram.")
if qtd != len(resultados):
    raise SystemExit(1)
