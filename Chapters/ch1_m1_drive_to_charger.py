# ─────────────────────────────────────────────────────────────────
#  Chapter 1  ·  Mission 1 — "Drive to the Power Room"
#  Load world:  chapter1_corridor.py
# ─────────────────────────────────────────────────────────────────
#
#  OBJECTIVE
#  Drive Robby north from her start position (2, 2) through the
#  yellow gateway and reach the orange Power Charger at the far end.
#
#  NEW CONCEPTS
#    import time           → loads the Python 'time' module
#    time.sleep(seconds)   → pauses the script for that many seconds
#    drive(linear, angular)
#        linear  : speed forward/backward  (-1.0 … +1.0)
#        angular : turning speed           (-1.0 left … +1.0 right)
#
#  HOW TO READ drive()
#    drive(0.4,  0.0)  →  forward at 40% speed, no turning
#    drive(0.0,  1.0)  →  spin right (clockwise) at 100%
#    drive(0.0,  0.0)  →  STOP  (always end your script with this!)
#    drive(-0.4, 0.0)  →  reverse at 40% speed
#
#  STEP-BY-STEP CHALLENGE
#  ───────────────────────
#  Step 1: Run this script as-is.  Does Robby reach the charger?
#          Watch the battery indicator in the sidebar.
#
#  Step 2: The sleep time might need tuning for your system.
#          If Robby stops short, increase 2.4 → 2.6 or 2.8.
#          If Robby hits the north wall, reduce it.
#
#  Step 3: Add a battery report after Robby stops:
#              print(f"Arrived. Battery: {battery_level()}%")
#
#  TIP — Why time.sleep?
#  drive() does NOT wait for Robby to travel a distance.
#  It sets Robby's speed and returns immediately.
#  time.sleep() is what keeps the motor running for a duration.
#  Think: "run engine for X seconds".
# ─────────────────────────────────────────────────────────────────

import time

# Report starting state
print(f"Mission start.  Battery: {battery_level()}%")
print("Driving north to the Power Room ...")

# Set speed forward, no angular velocity (straight line)
drive(0.4, 0.0)

# Keep driving for approximately 2.4 seconds.
# ← TUNE THIS: increase if Robby stops short of the charger,
#              decrease if Robby drives into the north wall.
time.sleep(2.4)

# Stop all motion
drive(0.0, 0.0)

# Report arrival
print(f"Arrived at Power Room.  Battery: {battery_level()}%")
print("Charging ...")
