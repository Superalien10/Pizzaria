def list_ingredientes(dict_ingredientes: dict[str, dict[str, float]], list_tipos: list[str] = ["massa", "molho", "queijo", "cobertura"]):
    """recebe um dicionario de ingredientes e imprime os ingredientes e os seus preços

    Args:
        dict_ingredientes (dict[str, dict[str, float]]): Um dicionario que tem como chave
        o tipo do ingrediente e como item dicionário que contém como chave o nome do ingrediente e como item o preço
        list_tipos (list[str], optional): lista dos tipos de ingredientes a serem listados. Deve ser do tipo "massa", "molho", "queijo" ou "cobertura". Defaults to ["massa", "molho", "queijo", "cobertura"].
    """

def remover_ingrediente(ingrediente: str, dict_ingredientes: dict[str, dict[str,float]])-> dict[str, dict[str,float]]:
    """Remove um ingrediente dicion�rio de ingredientes cadastrados.
    Args:
        ingrediente (str): nome do ingrediente a ser adicionado.
        dict_ingredientes (dict[str, dict[str,float]]): Um dicionario que tem como chave
        o tipo do ingrediente e como item dicion�rio que cont�m como chave o nome do ingrediente e como item o pre�o.
    Returns:
        dict[str, dict[str,float]]: dicionario com o ingrediente removido
     
    >>> dict_ingredientes = {"massa": {"branca":2}, "molho":{"bolo":3, "calda":5}}
    >>> remover_ingrediente("bolo", dict_ingredientes
    {'massa': {'branca': 2}, 'molho': {'calda': 5}}
    >>> dict_ingredientes = {"massa": {"branca":2}, "molho":{"bolo":3, "calda":5}}
    >>> remover_ingrediente("jujuba", dict_ingredientes
     {"massa": {"branca":2}, "molho":{"bolo":3, "calda":5}}
    """
    for tipo in list(dict_ingredientes):
        for estocado in list(dict_ingredientes[tipo]):
            if ingrediente == estocado:
                aqui=dict_ingredientes[tipo]
                aqui.pop(ingrediente)
    return dict_ingredientes

def add_ingrediente(ingrediente: str, preco: float, tipo: str, dict_ingredientes: dict[str, dict[str,float]] = None) -> dict[str, dict[str,float]]:
    """recebe um dicionário de ingredientes e adiciona um novo ingrediente de um determinado tipo. Imprime o ingrediente, o tipo e o preço

    Args:
        ingrediente (str): nome do ingrediente a ser adicionado. Caso o ingrediente já exista, o preço é atualizado
        preco (float): preço do ingrediente.
        tipo (str): tipo do ingrediente. Deve ser 'massa', 'molho', 'queijo' ou 'cobertura', caso não seja um desses valores, não será adicionado.
        dict_ingredientes (dict[str, dict[str,float]], optional):  Um dicionario que tem como chave
        o tipo do ingrediente e como item dicionário que contém como chave o nome do ingrediente e como item o preço

    Returns:
        dict[str, dict[str,float]]: dicionário com o novo ingrediente adicionado
    """
    if tipo == 'massa' or tipo == 'molho' or tipo == 'queijo' or tipo == 'cobertura':
        dict_ingredientes[tipo][ingrediente] = preco
        print('ingrediente adicionado:', ingrediente)
        print('-'*42)
        print('tipo do ingrediente:', tipo)
        print('-'*42)
        print('preço do ingrediente:', preco)
        print('-'*42)
    else:
        print('tipo de ingrediente inválido')
        print('-'*42)
    
    print('dicionário de ingredientes',dict_ingredientes)
    return dict_ingredientes

def montar_pizza(dict_ingredientes: dict[str, dict[str,float]]) -> float:
    """Recebe um dicionário de ingredientes e calcula o preço da pizza. Imprime o dicionário de ingredientes e o valor da pizza

    Args:
        dict_ingredientes (dict[str, dict[str,float]]): Um dicionario que tem como chave
        o tipo do ingrediente e como item dicionário que contém como chave o nome do ingrediente e como item o preço

    Returns:
        float: preço da pizza
    """
    preco = 0
    for tipo in dict_ingredientes:
        for ingrediente in dict_ingredientes[tipo]:
            preco += dict_ingredientes[tipo]
    print('dicionário de ingredientes utilizados: ',dict_ingredientes)
    print('-'*42)
    return preco
#teste = {"massa": {"trigo": 4.0, "vagem": 4.0}, "molho": {"tomate": 5.0}, "queijo": {"musarela": 6.0}, "cobertura": {"milho": 4.0}}
