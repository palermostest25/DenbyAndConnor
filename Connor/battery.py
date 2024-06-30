import psutil
import subprocess
import time
import daemon

with daemon.DaemonContext():
    def send_notification(title, message, timeout=10):
        subprocess.run(['notify-send', title, message, '-t', str(timeout * 1000), '-u', 'critical'])

    def check_battery():
        while True:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = battery.percent

            if not plugged and percent < 36:
                send_notification(
                    title="Low Battery",
                    message="Your battery is low (below 35%). pls plug in your computer!",
                    timeout=10
                )

            if plugged and percent > 64:
                send_notification(
                    title="High Battery",
                    message="Your battery is high (above 65%). pls unplug your computer.",
                    timeout=10
                )

            time.sleep(60)

if __name__ == "__main__":
    while True:
        check_battery()
