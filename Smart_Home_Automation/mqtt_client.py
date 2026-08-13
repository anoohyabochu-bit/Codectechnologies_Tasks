import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883

MQTT_TOPIC = "smart_home/devices"


def connect_mqtt():
    client = mqtt.Client()

    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        print("Connected to MQTT broker")
        return client

    except Exception as error:
        print("MQTT connection failed:", error)
        return None


def publish_device_command(device_id, status):
    client = connect_mqtt()

    if client is None:
        return False

    message = f"{device_id}:{status}"

    client.publish(MQTT_TOPIC, message)

    client.disconnect()

    print("MQTT message sent:", message)

    return True