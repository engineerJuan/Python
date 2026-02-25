class Animal:
    def __init__(self, Especie, Nombre):
        self.Especie = Especie
        self.Nombre = Nombre

    def hablar(self):
        if self.Especie == 'Perro':
            print(f"{self.Nombre} (Perro) dice: Guau")
        elif self.Especie == 'Gato':
            print(f"{self.Nombre} (Gato) dice: Miau")
        elif self.Especie == 'Vaca':
            print(f"{self.Nombre} (Vaca) dice: Muu")
        elif self.Especie == 'Pato':
            print(f"{self.Nombre} (Pato) dice: Cuac")
        elif self.Especie == 'León':
            print(f"{self.Nombre} (León) dice: Roooar")
        else:
            print(f"{self.Nombre} ({self.Especie}) dice: ...")

Perro = Animal('Perro', 'Max')
Gato = Animal('Gato', 'Michi')
Vaca = Animal('Vaca', 'Lola')
Pato = Animal('Pato', 'Donald')
Leon = Animal('León', 'Simba')

Perro.hablar()
Gato.hablar()
Vaca.hablar()
Pato.hablar()
Leon.hablar()