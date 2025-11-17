def timpo_viaje():
    distancia = int(input("Escribe La Distancia:"))
    velocidad = int(input("Escribe La Velocidad:"))

    return distancia / velocidad

resultado = timpo_viaje()
print(resultado, "Horas")