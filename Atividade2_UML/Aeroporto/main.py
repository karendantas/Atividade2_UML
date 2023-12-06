from Questão_aeroposto import *


#Aeroporto
Aeroporto1 = Aeroporto("Vuador", "Coitadolandia", 10)

#Voo
Voo1 = Voo(300, "Internacional", 3339, "09/10/2030", Aeroporto1, "Darcinópolis")

#Funcionarios(Op e aeroviários):
Operario1 = Operadores("Luzi", 1400)
aero1 = Aeroviários("Bilu", 1222)
aero2 = Aeroviários("Bendito",1122)
aero3 = Aeroviários("Bincolus", 1222)

#Tripulação
Voo1.Tripulação.add_aero(aero1)
Voo1.Tripulação.add_aero(aero2)
Voo1.Tripulação.add_aero(aero3)

#passageiros
p1 = Passageiro("Cleia", 33,True)



# print(Voo1.mostrarTripulação())
print(Voo1.reservas)
p1.criarReserva(12, Voo1)
print(p1.reserva.Voo_Ref)
Operario1.criarReservaOP(p1, 12, Voo1)
print(Voo1.reservas)
