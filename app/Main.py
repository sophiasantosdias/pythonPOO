from Cliente import Cliente
from Conta import Conta

class Main:
    pass

c1 = Cliente('João', '2199999-9999')
conta = Conta(c1.get_nome(), 1222)

conta.deposita(100)
conta.saque(50)
conta.extrato()
