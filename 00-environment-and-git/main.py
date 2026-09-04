# Data of Mission Countdown is being extracted from the following source: https://go4liftoff.com/ , tool of https://thespacedevs.com/llapi.

from datetime import datetime
import time
import zoneinfo
from dataclasses import dataclass

@dataclass
class MissionCountdown:
    def __init__(self):
        self.MissionName: (str) = "Long March 8A | Unknown Payload"
        self.MissionDescription: str = "The Long March 8A is a Chinese orbital launch vehicle developed by the China Academy of Launch Vehicle Technology (CALT). It is designed to carry payloads into low Earth orbit (LEO) and sun-synchronous orbit (SSO). The Long March 8A is part of the Long March family of rockets, which have been used for various space missions since the 1970s."
        self.MissionDate: int = datetime(2026, 9, 11, 18, tzinfo=zoneinfo.ZoneInfo("Europe/Madrid")).timestamp()  # September 11, 2026, at 18:00 CEST and its timestamp
mission = MissionCountdown()

mission_name = input("Enter the mission name, or press Enter to keep the default: ").strip()
if mission_name:
    mission.MissionName = mission_name

mission_description = input("Enter the mission description, or press Enter to keep the default  : ").strip()
if mission_description:
    mission.MissionDescription = mission_description

mission_date = input("Enter the mission date (YYYY-MM-DD HH:MM:SS, or press Enter to keep the default): ").strip()

if mission_date:
    date_object = datetime.strptime(
        mission_date,
        "%Y-%m-%d %H:%M:%S"
    )

    date_object = date_object.replace(
        tzinfo=zoneinfo.ZoneInfo("Europe/Madrid")
    )

    mission.MissionDate = int(date_object.timestamp())

print(f"Mission Name: {mission.MissionName}")
print("-" * 50)
print(f"Mission Description: {mission.MissionDescription}")
print("-" * 50)
print(f"Mission Date: {datetime.fromtimestamp(mission.MissionDate, tz=zoneinfo.ZoneInfo('Europe/Madrid')).strftime('%Y-%m-%d %H:%M:%S %Z')}")
print("-" * 50)

CurrentDate: int = datetime.now().timestamp()  # Current date and time in timestamp format

# Time left until the mission in hours, minutes, and seconds.

try:
    TimeLeft = mission.MissionDate - CurrentDate

except:
    TimeLeft = 0

if TimeLeft <= 0:
    print("The mission has already occurred.")

print("Countdown:")
print(f"Days Left: {int(TimeLeft // 86400)} | Hours Left: {int(TimeLeft // 3600)} | Minutes Left: {int((TimeLeft % 3600) // 60)} | Seconds Left: {int(TimeLeft % 60)}")