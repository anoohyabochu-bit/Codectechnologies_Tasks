from flask import Flask, render_template, request, redirect, jsonify

from database import (
    initialize_database,
    get_devices,
    update_device_status,
    add_schedule,
    get_schedules,
    delete_schedule
)

from mqtt_client import publish_device_command
from scheduler import start_scheduler


app = Flask(__name__)


# Initialize database
initialize_database()

# Start scheduler
start_scheduler()


@app.route("/")
def home():

    devices = get_devices()
    schedules = get_schedules()

    return render_template(
        "index.html",
        devices=devices,
        schedules=schedules
    )


@app.route("/toggle/<int:device_id>", methods=["POST"])
def toggle_device(device_id):

    devices = get_devices()

    device = None

    for item in devices:
        if item["id"] == device_id:
            device = item
            break

    if device is None:
        return jsonify({
            "success": False,
            "message": "Device not found"
        })

    if device["status"] == "ON":
        new_status = "OFF"
    else:
        new_status = "ON"

    update_device_status(device_id, new_status)

    # Send MQTT command
    publish_device_command(device_id, new_status)

    return jsonify({
        "success": True,
        "status": new_status
    })


@app.route("/schedule", methods=["POST"])
def schedule_device():

    device_id = request.form.get("device_id")
    action = request.form.get("action")
    schedule_time = request.form.get("schedule_time")

    if not device_id or not action or not schedule_time:
        return redirect("/")

    add_schedule(
        device_id,
        action,
        schedule_time
    )

    return redirect("/")


@app.route("/delete_schedule/<int:schedule_id>", methods=["POST"])
def remove_schedule(schedule_id):

    delete_schedule(schedule_id)

    return redirect("/")


if __name__ == "__main__":

    print("Smart Home Automation System started.")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=False
    )