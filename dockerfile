# Usar la imagen base de Python
FROM python:3.9.11

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de dependencias y luego instalar las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Copiar el código fuente de la aplicación
COPY . /app/

# Exponer el puerto en el que correrá la aplicación (generalmente 8000 para Django)
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
