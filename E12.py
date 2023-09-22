nombre_archivo = input("Ingrese el nombre del archivo: ")

extensiones_mime = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

extension = nombre_archivo.split(".")[-1].lower()
tipo_mime = extensiones_mime.get(extension, "application/octet-stream")
print(f"El tipo de archivo MIME para '{nombre_archivo}' es: {tipo_mime}")
