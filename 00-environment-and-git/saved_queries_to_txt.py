import datetime
import zoneinfo
from pathlib import Path

path = Path(__file__).resolve().parent / "query-history.txt"

def save_query(mission_name, mission_description, mission_date, time_left):
    with path.open("a", encoding="utf-8") as file:
        file.write("\n" + "=" * 50 + "\n")
        file.write(f"Mission Name: {mission_name}\n")
        file.write("-" * 50 + "\n")
        file.write(f"Mission Description: {mission_description}\n")
        file.write("-" * 50 + "\n")
        file.write(
            "Mission Date: "
            f"{datetime.datetime.fromtimestamp(mission_date, tz=zoneinfo.ZoneInfo('Europe/Madrid')).strftime('%Y-%m-%d %H:%M:%S %Z')}\n"
        )
        file.write("-" * 50 + "\n")
        file.write("Countdown:\n")
        file.write(
            f"Days Left: {int(time_left // 86400)} | "
            f"Hours Left: {int(time_left // 3600)} | "
            f"Minutes Left: {int((time_left % 3600) // 60)} | "
            f"Seconds Left: {int(time_left % 60)}\n"
        )

