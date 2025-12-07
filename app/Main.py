class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1 = Cliente('João', '2199574-7849')
conta = Conta(c1.nome, 6565, 0)

print(f'Conta de {conta.titular}, número {conta.numero} com saldo de {conta.saldo}')
