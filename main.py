# Bank System

"""
PyBankSystem - Sistema bancário simples em Python
Autor: Matheus Camargo
GitHub: https://github.com/matheusc9
Data: 21/05/2025

Descrição:
Sistema que simula operações bancárias básicas como criação de contas,
depósitos, saques, transferências e consultas de saldo e extrato.

Licença: MIT
"""

class bank_account:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
    
    def menu(self, contas, my_id):
        print("- RedBank")
        print(f"\nBem-vindo, {self.nome}!")
        print(f"\nSaldo: R${self.saldo}")
        print("\n1) Depositar | 2) Transferir | 3) Voltar")
        option = input("Opção: ")
        if option == "1":
            self.depositar(contas, my_id)
        elif option == "2":
            if self.saldo <= 0:
                print("Você não possui saldo suficiente!")
                self.menu(contas, my_id)
            self.transferir(contas, my_id)
        elif option == "3":
            return
        else:
            print("Opção inválida!")
            self.menu(contas, my_id)


    def depositar(self, contas, my_id):
        print("\n- Depósito -")
        deposito = float(input("Valor: R$"))
        if deposito < 1:
            print("\nValor inválido!")
            self.depositar()
        self.saldo += float(deposito)
        print(f"Depósito concluído: {deposito} para {contas[my_id].nome}")
        self.menu(contas, my_id)

    def transferir(self, contas, my_id):
        print("- Transferência -\n")
        valort = float(input("Valor: R$"))
        if valort > self.saldo:
            print("Você não possui esse valor!")
            return self.transferir(contas, my_id)
        elif valort < 1:
            print("Valor inválido!")
            return self.transferir(contas, my_id)

        destino_id = input("Destino(ID): ")
        if destino_id not in contas:
            print("Id inválido ou inexistente!")
            return self.transferir(contas, my_id)
        if destino_id == my_id:
            print("Você não pode transferir para si mesmo!")
            return self.transferir(contas, my_id)

        self.saldo -= valort
        contas[destino_id].saldo += valort
        print(f"Transferência concluída: {valort} para {contas[destino_id].nome}")

        self.menu(contas, my_id)


class bank:
    def __init__(self):
        self.contas = {
            "1": bank_account("Alice Oliveira", 150.0),
            "2": bank_account("Bruno Santos", 200.0),
            "3": bank_account("Carla Veiga", 300.0),
            "4": bank_account("Diego Silva", 450.0),
            "5": bank_account("Elisa Pereira", 500.0),
        }

    def login(self):
        print("- RedBank")
        print("\nFaça login")
        id = input("Digite o ID: ")
        if id in self.contas:
            conta = self.contas[id]
            conta.menu(self.contas, id)
        else:
            print("ID inválido.")
            return self.login()


                                                                                                                                                                                                                                                                                                                                                                  # Hi, this not a malware :) | mc9
banco = bank()

while True:
    banco.login()
