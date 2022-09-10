from clientes import Cliente
from contas import Conta

# Crie um software de gerenciamento bancário.
# Esse software poderá ser capaz de criar clientes e contas.
# Cada cliente possui nome, cpf e idade.
# Cada conta possui um cliente e saldo.
# Os métodos serão: sacar, depositar e consultar saldo



Cliente01 = Cliente("Luan","12345678910",24)

Conta_Cliente01 = Conta(Cliente01,100)

print(Cliente01)

print(Conta_Cliente01.consultar_saldo())

Conta_Cliente01.depositar(400)

print(Conta_Cliente01.consultar_saldo())

Conta_Cliente01.sacar(250)

print(Conta_Cliente01.consultar_saldo())

