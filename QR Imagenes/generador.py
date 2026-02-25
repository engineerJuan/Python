import qrcode
from PIL import Image
import os

def generar_qr_con_logo(datos, ruta_logo, ruta_salida):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(datos)
    qr.make(fit=True)

    img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    if not os.path.exists(ruta_logo):
        print(f"Error: No se encontró la imagen en '{ruta_logo}'.")
        return

    logo = Image.open(ruta_logo)

    # Calcular tamaño del logo
    ancho_qr, alto_qr = img_qr.size
    factor_tamano = 3.5 
    ancho_logo = int(ancho_qr // factor_tamano)
    alto_logo = int(alto_qr // factor_tamano)

    proporcion_logo = logo.size[0] / logo.size[1]
    if proporcion_logo > 1:
        alto_logo = int(ancho_logo / proporcion_logo)
    else:
        ancho_logo = int(alto_logo * proporcion_logo)

    logo = logo.resize((ancho_logo, alto_logo), Image.Resampling.LANCZOS)

    # CREAR MARCO BLANCO
    borde = 15 # Grosor del marco blanco
    fondo_blanco = Image.new('RGB', (ancho_logo + borde * 2, alto_logo + borde * 2), 'white')
    
    if logo.mode in ('RGBA', 'LA') or (logo.mode == 'P' and 'transparency' in logo.info):
        logo = logo.convert("RGBA")
        fondo_blanco.paste(logo, (borde, borde), logo)
    else:
        fondo_blanco.paste(logo, (borde, borde))

    # Pegar el marco blanco (con la imagen adentro) en el centro del QR
    pos_x = (ancho_qr - fondo_blanco.size[0]) // 2
    pos_y = (alto_qr - fondo_blanco.size[1]) // 2
    img_qr.paste(fondo_blanco, (pos_x, pos_y))

    img_qr.save(ruta_salida)
    print(f"¡Éxito! Código QR con imagen guardado en: {ruta_salida}")

if __name__ == "__main__":
    texto_qr = "https://mxdxvxlopxr.netlify.app/"
    
    # Escribe aquí el nombre exacto de la imagen que metiste en esta carpeta
    archivo_logo = "mi_logo.png" 
    archivo_salida = "qr_con_imagen_mejorado.png"

    generar_qr_con_logo(texto_qr, archivo_logo, archivo_salida)