# ─────────────────────────────────────────────────────────────────
#  Chapter 1  ·  Mission 3 — "One Change, Big Difference"
#  Load world:  chapter1_corridor.py
# ─────────────────────────────────────────────────────────────────
#
#  OBJECTIVE
#  Understand WHY variables exist by seeing what happens when you
#  change a single value and run the same program.
#
#  THE MISSION
#  ───────────
#  1. Run this script.  Observe Robby's speed.
#     Note: all three actions use the same SPEED variable.
#
#  2. Change  SPEED = 0.4  to  SPEED = 0.2  and run again.
#     Every action slows down at once.  You changed ONE line.
#
#  3. Change  SPEED = 0.7  and run again.  Robby is now much faster.
#     Still only ONE change.
#
#  4. Now imagine the script had  0.4  written 10 times instead of
#     a variable.  How many lines would you need to change?
#     THIS is why variables exist.
#
#  KEY INSIGHT
#  A variable lets you control a value used in many places
#  by changing it in exactly one place.
#  Name your variables clearly so the next person (or future you!)
#  understands what the value means.
#
#  CHALLENGE
#  Add a second variable  TURN_SPEED = 0.8  and use it for all
#  three turning commands.  Change TURN_SPEED independently of SPEED
#  and observe the effect.
# ─────────────────────────────────────────────────────────────────

import time

# ── Change ONLY this one value — everything below adapts ─────────
SPEED = 0.4    # ← try 0.2, 0.4, 0.6, 0.8

# ─────────────────────────────────────────────────────────────────
print(f"Mission 3 start.  Speed = {SPEED}  Battery: {battery_level()}%")

# Action 1: short burst forward
print("Action 1: burst forward")
drive(SPEED, 0.0)
time.sleep(1.5)
drive(0.0, 0.0)
time.sleep(0.3)

# Action 2: turn right
print("Action 2: right turn")
drive(0.0, SPEED)          # using SPEED for turning too — notice the difference!
time.sleep(0.5)
drive(0.0, 0.0)
time.sleep(0.3)

# Action 3: drive forward again
print("Action 3: forward again")
drive(SPEED, 0.0)
time.sleep(1.5)
drive(0.0, 0.0)

print(f"Done.  Battery: {battery_level()}%")
print(f"The whole behaviour changed — and you only edited one line.")
