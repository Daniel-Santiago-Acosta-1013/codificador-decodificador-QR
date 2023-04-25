import qrcode
from PIL import Image
import argparse

def generate_qr_code(data: str, file_name: str) -> None:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

def main():
    parser = argparse.ArgumentParser(description="Genera un código QR para texto, imágenes, videos o audio.")
    parser.add_argument("format", choices=["texto", "imagen", "video", "audio"], help="El formato del contenido a codificar.")
    parser.add_argument("data", help="El contenido a codificar o la URL del archivo multimedia.")
    parser.add_argument("file_name", default="qr_code.png", nargs="?", help="El nombre del archivo donde se guardará el código QR.")
    
    args = parser.parse_args()

    generate_qr_code(args.data, args.file_name)
    print(f"Código QR generado y guardado como {args.file_name}")

if __name__ == "__main__":
    main()
