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
        self.reservas = []*300

    def mostrarTripulação(self):
        for t in self.Tripulação.conjunto_aero:
            print(t.nome)


class Passageiro:
    def __init__(self, nome,idade, passaporte=True):
        self.nome = nome
        self.idade = idade
        self.passaporte = passaporte
        self.reserva = None

    def possuiReserva(self):
        if self.reserva is not None:
            return True

    def criarReserva(self, numero, voo):
        if self.possuiReserva() is not True:
            self.reserva = Reserva(numero,voo, Passageiro)
        return self.reserva
    
    def pagarReserva(self):
        self.reserva.pago = True
        print("Pagamento realizado")
        return self.reserva.pago
    
    def cancelarReserva(self, numero):
        if numero == self.reserva.numero_reserva():
            self.reserva = None
        return self.reserva

class Reserva:
    def __init__(self, numero_reserva,passageiro, Voo_Ref, pago=None):
        self.numero_reserva = numero_reserva
        self.passageiro = passageiro
        self.Voo_Ref = Voo_Ref
        self.pago = pago

    def pagamentoConfirmado(self):
        if self.pago == True:
            print("Pagamento confirmado")


class Funcionário:
    def __init__(self, nome, salário):
        self.nome = nome
        self.salario = salário


class Operadores(Funcionário):
    def __init__(self, nome, salário, voo):
        super().__init__(nome, salário)
        self.voo_pertencente = voo

    def criarReservaOP(self, passageiro, numero, voo):
        if passageiro.reserva is None:
            res =  passageiro.criarReserva(numero)
            return voo.reservas.append(res)
        else:
            return voo.reservas.append(passageiro.reserva)

    def cancelarReservaOP(self, passageiro, numero, voo):
        if passageiro.possuiReserva() is True:
            res = passageiro.cancelarReserva(numero)
            return voo.reservar.remove(res)
        else:
            return voo.reservar.append(passageiro.reserva())
    
class Aeroviários(Funcionário):
    pass

class ConjuntoAeroviários:
    conjunto_aero = []
    def __init__(self):
        pass

    def add_aero(self, aeroviário):
        self.conjunto_aero.append(aeroviário)


