# sistema_bancario_poo/main.py
from cliente import Cliente
from conta import ContaCorrente
from banco import Banco

# Criando instâncias de clientes
cliente1 = Cliente("João Silva", "123.456.789-00")
cliente2 = Cliente("Maria Souza", "987.654.321-00")

# Criando contas
conta1 = ContaCorrente(cliente1)
conta2 = ContaCorrente(cliente2)

# Criando banco
banco = Banco("Banco Dio")
banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)

# Operações
conta1.depositar(1000)
conta1.sacar(200)
conta1.transferir(300, conta2)

print("\nExtrato João:")
conta1.imprimir_extrato()

print("\nExtrato Maria:")
conta2.imprimir_extrato()
