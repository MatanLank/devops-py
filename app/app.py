from flask import Flask, request
import socket
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    container_name = socket.gethostname()

    weather = requests.get(
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=32.0853&longitude=34.7818&current_weather=true",
        timeout=5
    ).json()

    temperature = weather["current_weather"]["temperature"]

    return f"""
    <h2>Hello {client_ip} and welcome to Silverfort’s {container_name}</h2>
    <p>Current Temperature in Tel-Aviv is {temperature}°C</p>
    """

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8443,
        ssl_context=("cert.pem", "key.pem")
    )

