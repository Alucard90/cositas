from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guardar', methods=['GET'])
def guardar():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    mensaje = f"""
    📅 Fecha: {fecha}
    🌐 IP: {ip}
    📍 Latitud: {lat}
    📍 Longitud: {lon}
    """

    # Guardar en archivo
    with open('ubicaciones.txt', 'a') as f:
        f.write(mensaje + '\n')

    return 'Ubicación recibida. ¡Gracias!'