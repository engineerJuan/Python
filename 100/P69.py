def tasa_desempleo(desempleados, empleados):
    return(desempleados / empleados) * 100

resultado = tasa_desempleo(100, 900)
print(resultado)