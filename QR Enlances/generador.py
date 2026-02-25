import qrcode

def generar_qr_simple(datos, ruta_salida):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(datos)
    qr.make(fit=True)

    img_qr = qr.make_image(fill_color="black", back_color="white")
    img_qr.save(ruta_salida)
    print(f"¡Éxito! Código QR de enlace guardado en: {ruta_salida}")

if __name__ == "__main__":
    # Tu enlace web
    texto_qr = "https://mxdxvxlopxr.netlify.app/"
    archivo_salida = "QR.png"

    generar_qr_simple(texto_qr, archivo_salida)