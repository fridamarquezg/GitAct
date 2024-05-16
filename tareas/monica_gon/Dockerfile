# Usa la imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo .py actual al directorio de trabajo en la imagen
COPY prueba.py /app

# Instala las dependencias necesarias
RUN pip install polars pandas

# Ejecuta el archivo .py cuando se inicie el contenedor
CMD ["python", "prueba.py"]
