import json
import time
import paho.mqtt.client as mqtt


# ==========================================
# MQTT CONFIGURATION
# ==========================================

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883

MQTT_TOPIC = "smart_home/devices"


# ==========================================
# VIRTUAL DEVICES
# ==========================================

devices = {
    1: {
        "name": "Living Room Light",
        "type": "LIGHT",
        "status": "OFF"
    },

    2: {
        "name": "Bedroom Light",
        "type": "LIGHT",
        "status": "OFF"
    },

    3: {
        "name": "Living Room Fan",
        "type": "FAN",
        "status": "OFF"
    },

    4: {
        "name": "Kitchen Light",
        "type": "LIGHT",
        "status": "OFF"
    }
}


# ==========================================
# DISPLAY DEVICES
# ==========================================

def show_devices():

    print()
    print("=" * 55)
    print("       VIRTUAL RASPBERRY PI - DEVICES")
    print("=" * 55)

    for device_id, device in devices.items():

        print(
            f"{device_id}. "
            f"{device['name']:20} "
            f"Status: {device['status']}"
        )

    print("=" * 55)
    print()


# ==========================================
# UPDATE DEVICE
# ==========================================

def update_device(device_id, status):

    if device_id not in devices:

        print(f"Unknown device ID: {device_id}")

        return

    status = status.upper()

    if status not in ["ON", "OFF"]:

        print(f"Invalid status: {status}")

        return

    devices[device_id]["status"] = status

    device_name = devices[device_id]["name"]

    print()
    print("****************************************")
    print("        VIRTUAL DEVICE UPDATED")
    print("****************************************")

    print(f"Device : {device_name}")
    print(f"Status : {status}")

    if status == "ON":

        print("💡 Virtual device is now ON")

    else:

        print("⚫ Virtual device is now OFF")

    print("****************************************")

    show_devices()


# ==========================================
# PARSE MQTT MESSAGE
# ==========================================

def process_message(message):

    print()
    print("MQTT MESSAGE RECEIVED")
    print("---------------------")
    print("Raw message:", message)

    # --------------------------------------
    # Format 1:
    # 1:ON
    # --------------------------------------

    if ":" in message:

        parts = message.split(":")

        if len(parts) == 2:

            try:

                device_id = int(parts[0])

                status = parts[1].strip()

                update_device(device_id, status)

                return

            except ValueError:

                pass


    # --------------------------------------
    # Format 2:
    # 1,ON
    # --------------------------------------

    if "," in message:

        parts = message.split(",")

        if len(parts) == 2:

            try:

                device_id = int(parts[0])

                status = parts[1].strip()

                update_device(device_id, status)

                return

            except ValueError:

                pass


    # --------------------------------------
    # Format 3:
    # JSON
    #
    # {"device_id":1,"status":"ON"}
    # --------------------------------------

    try:

        data = json.loads(message)

        if isinstance(data, dict):

            device_id = data.get("device_id")

            status = data.get("status")

            if device_id is not None and status is not None:

                update_device(
                    int(device_id),
                    str(status)
                )

                return

    except Exception:

        pass


    print()
    print("Could not understand MQTT message.")
    print("Expected examples:")
    print("1:ON")
    print("1:OFF")
    print('{"device_id":1,"status":"ON"}')


# ==========================================
# MQTT CALLBACK
# ==========================================

def on_connect(client, userdata, flags, reason_code, properties):

    if reason_code == 0:

        print()
        print("==========================================")
        print("     VIRTUAL RASPBERRY PI STARTED")
        print("==========================================")

        print("MQTT Broker :", MQTT_BROKER)
        print("MQTT Topic  :", MQTT_TOPIC)

        print()
        print("Connected to MQTT broker successfully!")

        client.subscribe(MQTT_TOPIC)

        print()
        print("Subscribed to:")
        print(MQTT_TOPIC)

        show_devices()

        print("Waiting for commands from dashboard...")
        print()


    else:

        print()
        print("MQTT connection failed.")
        print("Reason:", reason_code)


# ==========================================
# MQTT MESSAGE CALLBACK
# ==========================================

def on_message(client, userdata, message):

    try:

        received_message = message.payload.decode("utf-8")

        process_message(received_message)

    except Exception as error:

        print("Error processing MQTT message:")
        print(error)


# ==========================================
# MQTT CLIENT
# ==========================================

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message


# ==========================================
# CONNECT TO BROKER
# ==========================================

print()
print("Connecting to MQTT broker...")
print()


try:

    client.connect(
        MQTT_BROKER,
        MQTT_PORT,
        60
    )

except Exception as error:

    print("Could not connect to MQTT broker.")
    print("Error:", error)

    print()
    print("Check your internet connection.")

    exit()


# ==========================================
# START MQTT LOOP
# ==========================================

try:

    client.loop_forever()

except KeyboardInterrupt:

    print()
    print("Virtual Raspberry Pi stopped.")

    client.disconnect()