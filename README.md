# Codificador y decodificador de código QR

Este es un ejemplo de un codificador y decodificador de código QR desarrollado en Python. El proyecto está dividido en dos archivos: `encoder.py` para codificar y `decoder.py` para decodificar.

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalado Python 3 y las siguientes dependencias:

- qrcode
- opencv-python
- pyzbar

Puedes instalar estas dependencias utilizando el archivo `requirements.txt` incluido en el proyecto:


```bash
$ pip install -r requirements.txt
```

## Uso

Para codificar un texto en un código QR, ejecuta el archivo `encoder.py` desde la línea de comandos proporcionando los argumentos necesarios:

```bash
python encoder.py <format> <data> [file_name]
```

* `<format>`: El formato del contenido a codificar. Puede ser `texto`, `imagen`, `video` o `audio`.
* `<data>`: El contenido a codificar o la URL del archivo multimedia.
* `[file_name]`: (Opcional) El nombre del archivo donde se guardará el código QR. Por defecto, se guardará como `qr_code.png`.

## Ejemplo

Para generar un código QR con una URL de imagen:

```bash
python script.py imagen https://example.com/image.jpg qr_code.png
```

Para decodificar un código QR desde un archivo de imagen, ejecuta el archivo `decoder.py` y sigue las instrucciones en la terminal:


```bash
$ python decoder.py
```

El programa te pedirá que ingreses el nombre del archivo de imagen que contiene el código QR. Si el código QR puede ser decodificado, el programa imprimirá el texto correspondiente en la terminal.

## Contribuir

Si deseas contribuir a este proyecto, siéntete libre de hacer un fork del repositorio y enviar un pull request con tus cambios. Asegúrate de seguir las buenas prácticas de programación y documentación. 

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.



