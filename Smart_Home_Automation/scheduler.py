from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

from database import get_schedules, update_device_status
from mqtt_client import publish_device_command


scheduler = BackgroundScheduler()


def check_schedules():
    current_time = datetime.now().strftime("%H:%M")

    schedules = get_schedules()

    for schedule in schedules:

        schedule_time = schedule["schedule_time"]

        if schedule_time == current_time:

            device_id = schedule["device_id"]
            action = schedule["action"]

            update_device_status(device_id, action)

            publish_device_command(device_id, action)

            print(
                f"Scheduled action executed: "
                f"{schedule['name']} -> {action}"
            )


def start_scheduler():
    scheduler.add_job(
        check_schedules,
        "interval",
        seconds=30
    )

    scheduler.start()

    print("Scheduler started.")