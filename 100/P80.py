import psutil

def obtener_ram():
    memoria = psutil.virtual_memory()

    memoria_total = memoria.total / (1024 ** 3)
    return memoria_total

memoria = obtener_ram()
print(f'Tu Memoria RAM es de {memoria:.2f} GB')