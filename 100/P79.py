class Cuenta:
    def __init__(self, Titular, Saldo):
        self.Titular = Titular
        self.Saldo = Saldo

    def Depositar(self, Cantidad):
        self.Saldo += Cantidad
        print('Se Deposito: ', Cantidad)

    def Retirar(Self, Cantidad):
        Self.Saldo -= Cantidad
        print('Se Retiro: ', Cantidad)

    def Mostrar(self):
        print(self.__dict__)

Cuenta1 = Cuenta('Juan', 10000)
Cuenta1.Mostrar()
Cuenta1.Depositar(90000)

Cuenta1.Mostrar()
Cuenta1.Retirar(20000)

Cuenta1.Mostrar()