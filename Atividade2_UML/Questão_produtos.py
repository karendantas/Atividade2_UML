
class Produto:
    def __init__(self, codigo, valor, descricao):
        self.__codigo = codigo
        self.__valor = valor
        self.__descricao =  descricao

    def getcodigo(self):
        return self.__codigo
    def getvalor(self):
        return self.__valor


#na agregação bota os objetos pra dentro da classe que esta se associando

class ItemPedido:
    def __init__(self, quantidade, produto):
        self.__quantidade = quantidade
        self.__itemProduto = produto
    
    def getquantidade(self):
        return self.__quantidade
    def getproduto(self):
        return self.__itemProduto
    
class Pedido:
    def __init__(self, quantidade_produto=0, produto=None):
        self.__itemPedido = ItemPedido(quantidade_produto, produto)
        self.__valortotal = 0
        self.__lista_pedidos = [produto]

    
    def adicionar_item(self, quantidade_produto, produto):
        self.__itemPedido = ItemPedido(quantidade_produto, produto)
        self.__lista_pedidos.append(produto)
        print( "Item adicionado")

    def obterTotal(self):
        self.__valortotal += self.__itemPedido.getquantidade() * self.__itemPedido.getproduto().getvalor()
        return self.__valortotal
    
    def retirar_item(self, produto, quantidade_produto):
        if produto in self.__lista_pedidos:
            self.__lista_pedidos.remove(produto)
            self.__valortotal -= produto.getvalor()*quantidade_produto
        return self.__valortotal

    def mostrarCarrinho(self):
        for i in self.__lista_pedidos:
            print(i.getcodigo())
    

#Pedidos
arroz = Produto(1,10.00, "Arroz branco")
feijao = Produto(2, 15.00, "Feijão carioca")
frango = Produto(3, 20.00, "Peito de frango")


pedido1 = Pedido(10, feijao)
print(pedido1.obterTotal())
pedido1.adicionar_item(2,frango)
print(pedido1.obterTotal())
pedido1.adicionar_item(4,arroz)
print(pedido1.obterTotal())
pedido1.mostrarCarrinho()
pedido1.retirar_item(feijao, 9)
print(pedido1.obterTotal())
pedido1.mostrarCarrinho()
