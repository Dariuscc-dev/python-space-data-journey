# Data of Mission Countdown is being extracted from the following source: https://go4liftoff.com/

from datetime import datetime
import time
import zoneinfo
from dataclasses import dataclass

@dataclass
class MissionCountdown:
    MissionName: str = "Long March 8A | Unknown Payload"
    MissionDescription: str = "The Long March 8A is a Chinese orbital launch vehicle developed by the China Academy of Launch Vehicle Technology (CALT). It is designed to carry payloads into low Earth orbit (LEO) and sun-synchronous orbit (SSO). The Long March 8A is part of the Long March family of rockets, which have been used for various space missions since the 1970s."
    MissionDate: int = datetime(2026, 9, 11, 18, tzinfo=zoneinfo.ZoneInfo("Europe/Madrid")).timestamp()  # September 11, 2026, at 18:00 CEST and its timestamp

CurrentDate: int = datetime.now().timestamp()  # Current date and time in timestamp format

# Time left until the mission in hours, minutes, and seconds.

try:
    TimeLeft = MissionCountdown.MissionDate - CurrentDate

except:
    TimeLeft = 0


print(f"Days Left: {int(TimeLeft // 86400)} | Hours Left: {int(TimeLeft // 3600)} | Minutes Left: {int((TimeLeft % 3600) // 60)} | Seconds Left: {int(TimeLeft % 60)}")
