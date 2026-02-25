class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre 
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":")
        print(".fuerza: ", self.fuerza)
        print(".inteligencia: ", self.inteligencia)
        print(".defensa: ", self.defensa)
        print(".vida: ", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):  
        print(f"{self.nombre} ha muerto")

    def daño(self, enemigo):
        return max(0, self.fuerza - enemigo.defensa) 

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}")
        if enemigo.esta_vivo():
            print(f"La vida de {enemigo.nombre} es {enemigo.vida}")
        else:
            enemigo.morir()

mi_personaje = Personaje("BitBoos", 10, 1, 5, 100)
mi_enemigo = Personaje("Enemy Stanto", 8, 5, 3, 100)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()