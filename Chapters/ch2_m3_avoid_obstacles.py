# ─────────────────────────────────────────────────────────────────
#  Chapter 2  ·  Mission 3 — "Navigate the Dark Room"
#  Load world:  chapter2_dark_room.py
# ─────────────────────────────────────────────────────────────────
#
#  OBJECTIVE
#  Robby must reach the orange Sensor_Charger in the NE corner of
#  the room — without touching a single obstacle.  She has no map.
#  She must sense, decide, and act on every step.
#
#  THE CONTROL LOOP
#  ────────────────
#  SENSE:   read distance(0)           ← what's ahead?
#  DECIDE:  if < SAFE: turn; else: go  ← decide what to do
#  ACT:     drive()                    ← execute the decision
#
#  This three-step pattern (Sense → Decide → Act) is the
#  foundation of ALL reactive robotics.
#
#  THE MISSION
#  ───────────
#  1. Run this script.  Watch Robby navigate.
#     Does she reach the orange charger?
#
#  2. Add a print() inside the loop to watch Robby's readings:
#       print(f"step={step}  gap={distance(0):.2f}")
#     What distance values trigger a turn?
#
#  3. Change  SAFE = 0.9  to  SAFE = 0.5  and run again.
#     Robby waits until obstacles are very close before turning.
#     Does she collide more often?
#
#  4. Change  SAFE = 1.8  and run again.
#     Robby turns very early.  Does she still reach the charger?
#
#  KEY INSIGHT
#  RIGHT BIAS (drive(0.4, 0.15)) makes Robby drift clockwise.
#  In a square room, clockwise drift eventually brings the robot
#  to the NE corner — where the charger lives.
#  This is not intelligence; it is geometry.
#
#  EXTENSION
#  Replace the fixed bias with sensor-guided steering:
#    if distance(90) > distance(270):
#        drive(0.4, 0.2)   # more open on right — drift right
#    else:
#        drive(0.4, -0.2)  # more open on left  — drift left
#  Does Robby reach the charger more reliably?
# ─────────────────────────────────────────────────────────────────

import time

# ── Tunable parameters ────────────────────────────────────────────
SAFE        = 0.9     # metres — turn if obstacle closer than this
TURN_TIME   = 0.12    # seconds per turn burst (try 0.08 and 0.18)
DRIVE_TIME  = 0.08    # seconds per forward burst
MAX_STEPS   = 400     # safety limit: stops after 400 cycles (≈ 40 s)

# ─────────────────────────────────────────────────────────────────
print(f"Avoidance mission start.  Battery: {battery_level()}%")
print("Target: orange Sensor_Charger in the NE corner.")
print(f"Safety distance: {SAFE} m")
print()

turns   = 0
forward = 0

for step in range(MAX_STEPS):
    gap = distance(0)

    if gap < SAFE:
        # Obstacle ahead — turn right until path clears
        drive(0.0, 1.0)
        time.sleep(TURN_TIME)
        turns += 1
    else:
        # Path clear — advance with slight rightward drift
        # (clockwise bias steers Robby toward the NE corner)
        drive(0.4, 0.15)
        time.sleep(DRIVE_TIME)
        forward += 1

drive(0.0, 0.0)
print()
print(f"Mission complete.  Steps run: {step + 1} / {MAX_STEPS}")
print(f"  Forward steps: {forward}   Turn steps: {turns}")
print(f"  Final battery: {battery_level()}%")
print()
print("Did Robby reach the Sensor_Charger?")
print("If battery is recharging, she made it!")
print("If she stopped short, try reducing SAFE or increasing MAX_STEPS.")
