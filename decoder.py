import cv2
from pyzbar.pyzbar import decode

def decode_qr_code(file_name: str) -> str:
    img = cv2.imread(file_name)
    decoded_objects = decode(img)

    if len(decoded_objects) > 0:
        return decoded_objects[0].data.decode("utf-8")
    else:
        return None

if __name__ == "__main__":
    file_name = input("Ingresa el nombre del archivo del código QR: ")
    decoded_data = decode_qr_code(file_name)
    
    if decoded_data:
        print(f"Dato decodificado: {decoded_data}")
    else:
        print("No se pudo decodificar el código QR.")
