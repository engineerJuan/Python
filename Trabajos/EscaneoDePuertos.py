import socket
import threading

def escanear_puerto(host, puerto, resultados):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            resultado = s.connect_ex((host, puerto))
            if resultado == 0:
                banner = ""
                try:
                    s.sendall(b'HEAD / HTTP/1.0\r\n\r\n')
                    banner = s.recv(1024).decode().strip()
                except:
                    banner = "No banner disponible"
                resultados[puerto] = banner
            else:
                resultados[puerto] = None
    except Exception as e:
        resultados[puerto] = None

def escanear_puertos(host, inicio, fin):
    print(f"Escaneando {host} del puerto {inicio} al {fin}...")
    threads = []
    resultados = {}

    for puerto in range(inicio, fin + 1):
        thread = threading.Thread(target=escanear_puerto, args=(host, puerto, resultados))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\nPuertos abiertos:")
    for puerto, banner in resultados.items():
        if banner is not None:
            print(f"Puerto {puerto} abierto - Banner: {banner}")

    print("\nPuertos cerrados o filtrados:")
    for puerto, banner in resultados.items():
        if banner is None:
            print(f"Puerto {puerto}")

if __name__ == "__main__":
    host = input("Introduce el host a escanear: ").strip()
    inicio = int(input("Puerto inicial: "))
    fin = int(input("Puerto final: "))

    escanear_puertos(host, inicio, fin)