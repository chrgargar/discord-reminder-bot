import requests
import time
import os
from datetime import datetime

# Configuración
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "https://discord.com/api/webhooks/1458411931022000277/YmbWLpOROBF1Yi1rXBbxLmrAZB99vbrk5EEQ15QOdASnOnIYWltO8Lzon3LQz-LwW34W")
INTERVALO_HORAS = 6

# Mensaje a enviar
MENSAJE = "@owner recuerda hacer up https://discord.com/channels/934267676354834442/1361039833765646406"


def enviar_mensaje():
    """Envía el mensaje al webhook de Discord."""
    data = {
        "content": MENSAJE,
        "username": "Recordatorio Bot"
    }

    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print(f"[{datetime.now()}] Mensaje enviado correctamente")
        else:
            print(f"[{datetime.now()}] Error al enviar: {response.status_code}")
    except Exception as e:
        print(f"[{datetime.now()}] Error: {e}")


def main():
    print(f"Bot iniciado - Enviando recordatorio cada {INTERVALO_HORAS} horas")
    print(f"Webhook configurado: {'Sí' if 'discord' in WEBHOOK_URL else 'No - Configura DISCORD_WEBHOOK_URL'}")

    # Enviar mensaje inicial
    enviar_mensaje()

    # Loop infinito
    while True:
        time.sleep(INTERVALO_HORAS * 60 * 60)  # Convertir horas a segundos
        enviar_mensaje()


if __name__ == "__main__":
    main()
