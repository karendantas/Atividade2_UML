import datetime

class Aeroporto:
    def __init__(self, nome, cidade, capacidade):
        self.nome = nome
        self.cidade = cidade
        self.capacidade = capacidade

class Voo:
    def __init__(self, assentos, Tipo, Código, Data, Aeroporto, destino):
        self.assentos = assentos
        self.Tripulação = ConjuntoAeroviários()
        self.Tipo = Tipo
        self.Codigo = Código
        self.Horário = datetime.datetime.date
        self.Data = Data
        self.Aeroporto = Aeroporto
        self.destino = destino
        self.reservas = []*self.assentos

    def mostrarTripulação(self):
        for t in self.Tripulação.conjunto_aero:
            print(t.nome)


# Como o modelo dizia que "Reservas possui um passageiro" fiz uma composição, onde o passageiro
# compoe a reserva. Logo se passageiro deixa de existir, a reserva não fará mais sentido.

#No entanto fiquei com uma dúvida, pois pesquisei alguns exemplos de composição e alguns traziam 
#o atributo inicilizando o prório objeto tipo: "self.passageiro = Passageiro()" e outros mostravam da
#forma que está na classe Reserva.
class Reserva:

    def __init__(self, numero_reserva, passageiro, Voo_Ref):
        self.numero_reserva = numero_reserva
        self.passageiro = passageiro
        self.Voo_Ref = Voo_Ref
     

class ManipularReservaMixIn:

    def criarReserva(self, numero, passageiro, Voo_ref):

        reserva = Reserva(numero, passageiro, Voo_ref)
        reserva.passageiro.reservas.append(reserva)

        '''Ao criar a reserva e identificar o Voo de referencia, o determinado Voo recebe em sua lista
        de reservas, a instancia criada'''
        Voo_ref.reservas.append(reserva)
        print("Reserva criada para o passageiro: {}".format(reserva.passageiro.nome))
        return True
    
    def pagarReserva(self, passageiro, numero):
        
        for r in passageiro.reservas:
             if  r.numero_reserva == numero:
                print("Pagamento realizado")
             

    def cancelarReserva(self, passageiro, numero):
       
        for r in passageiro.reservas:
            if  r.numero_reserva == numero:
                print("Reserva de número {} do passageiro: {} foi cancelada.".format(numero, passageiro.nome))
                passageiro.reservas.remove(r)
                Voo_ref = passageiro.reserva.r.Voo_ref
                Voo_ref.reservas.remove(r)
              
        
class Passageiro(ManipularReservaMixIn):
    def __init__(self, nome,idade, passaporte):
        self.nome = nome
        self.idade = idade
        self.passaporte = passaporte
        '''O passageiro pode ter nenhuma ou várias reservas ligadas ao seu nome'''
        self.reservas = []

class Funcionário:
    def __init__(self, nome, salário):
        self.nome = nome
        self.salario = salário


# Não entendi muito bem como essa classe deveria funcionar, então ela apenas recebe as mesmas funções
# do MixIn
class Operadores(Funcionário, ManipularReservaMixIn):
    def __init__(self, nome, salário):
        super().__init__(nome, salário)

    
class Aeroviários(Funcionário):
    pass

class ConjuntoAeroviários:
    conjunto_aero = []
    def __init__(self):
        pass

    def add_aero(self, aeroviário):
        self.conjunto_aero.append(aeroviário)


