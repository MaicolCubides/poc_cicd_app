# ----------- Stage 1: builder -----------
# version minimalista
FROM python:3.12-slim as builder 

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo del proyecto al contenedor
COPY requirements.txt .

# Instalamos las dependencias de python 
# --no-cache-dir evita que pip guarde cache, esto ayuda a reducir el tamaño de las imagenes
# --prefix=/install sirve para instalar esas libs en una ruta que no sea root
# para no generar errores a futuro con el usuario temporal
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ----------- Stage 2: runtime ----------- (Imagen final)
# Creamos una nueva imagen limpia (no tiene nada de build)
FROM python:3.12-slim

# Igual que antes, definimos el directorio de trabajo
WORKDIR /app

# copiar dependencias del builder
# Copiamos solo las dependencias instaladas desde la etapa builder
COPY --from=builder /install /usr/local

# copiar código 
COPY src ./src

# Agrega los binarios instalados por el pip al PATH
# Nos permite ejecutar comandos instaldos por pip, por ejemplo uvicorn, ya uvicorn queda en /root/.local/bin/uvicorn
# Util par que docker encuentre uvicorn
ENV PATH=/root/.local/bin:$PATH

# Ejecutamos el contenedor como ese usuario, para no usar root
# -m es para que quede en el home
RUN useradd -m appuser
USER appuser

# Abrimos el puerto realmente
EXPOSE 8000

# Esto es importante para kubernetes, docker ejecuta periódicamente: curl http://localhost:8000/health
# esto se usara en kubernetes, Docker Swarm, Orchestrators
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

# Definimos el comando que ejecuta el contenedor
# --host 0.0.0.0 permite contenedores fuera del contenedor, definimos el puerto
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]