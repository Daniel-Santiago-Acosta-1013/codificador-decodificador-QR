import qrcode
from PIL import Image

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

if __name__ == "__main__":
    data = input("Ingresa el texto para generar el código QR: ")
    file_name = "qr_code.png"
    generate_qr_code(data, file_name)
    print(f"Código QR generado y guardado como {file_name}")
