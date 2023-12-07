from Questão_aeroposto import *

#Aeroporto
Aeroporto1 = Aeroporto("Vuador", "Coitadolandia", 10)

#Voo
Voo1 = Voo(300, "Internacional", 3339, "09/10/2030", Aeroporto1, "Darcinópolis")
Voo2 = Voo(300, "Nacional", 222, "10,12,2024",Aeroporto1, "Fenda do Bikini")

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
p1.criarReserva(2, p1, Voo1)
print(Voo1.reservas)


#MENU
def menu ():
    opcao = 0
    while(opcao != 7):
        print("------------MENU-----------")
        print("1 - Cadastrar passageiro   ")
        print("2 - Cadastrar reserva")
        print("3 - Pagar Reserva    ")
        print("4 - Cancelar reserva")
        print("5 - Ver suas reservas")
        print("6 - Ver reservas de um Voo")
        print("7 - Sair")

        opcao = int(input("Digite sua opção:"))
        match (opcao):
            case 1:
                nome = input("Digite seu nome: ")
                idade = input("Informe sua idade: ")
                passaporte = input("Possui passaporte? S/N")
                Voo_referencia = input("Informe para qual Voo (Voo1 / Voo2):")
                if passaporte == 'S':
                    p1 = Passageiro(nome, idade, True)
                
                elif passaporte == 'N':
                    print("Passageiro deve possuir obrigatoriamente um passaporte.")
            case 2:
            
                Voo_referencia = input("Informe para qual Voo (Voo1 / Voo2):")
                if Voo_referencia == "Voo1":
                    p1.criarReserva(2, p1,Voo1)
                elif Voo_referencia== "Voo2":
                    p1.criarReserva(2,p1, Voo2)

            case 3:
                p1.pagarReserva()

            case 4:
                p1.cancelarReserva()

            case 5:
                
                for r in p1.reservas:
                    print(r)

            case 6:
                Voo_referencia = input("Informe o voo: ")
                if Voo_referencia == "Voo1":
                    for r in Voo1.reservas:
                        print(r)
                elif Voo_referencia == "Voo2":
                    for r in Voo2.reservas:
                        print(r)
            case 7:
                print("Saindo....")
                break


menu()