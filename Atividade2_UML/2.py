
class Produto:
    def __init__(self, codigo, valor, descricao):
        self.__codigo = codigo
        self.__valor = valor
        self.__descricao =  descricao


#na agregação bota os objetos pra dentro da classe que esta se associando

class ItemPedido:
    def __init__(self, quantidade, produto):
        self.__quantidade = quantidade
        self.__itemProduto = produto
    
class Pedido:
    def __init__(self):
        self.__lista_pedidos.append = []
        self.__valortotal = 0

    def adicionar_item(self, itemPedido):
        self.__lista_pedidos.append(itemPedido)
        print( "Item adicionado")

    def obterTotal(self):
        valor = 0
        for p in self.__lista_pedidos:
            valor += p.valor
        self.__valortotal = valor
        return self.__valortotal
    

#Pedidos
arroz = Produto(1,10.00, "Arroz branco")
feijao = Produto(2, 15.00, "Feijão carioca")
frango = Produto(3, 20.00, "Peito de frango")

carrinho1 = ItemPedido(10,feijao)
pedido1 = Pedido()
pedido1.adicionar_item(carrinho1)
print(pedido1.obterTotal())