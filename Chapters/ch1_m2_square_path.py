# ─────────────────────────────────────────────────────────────────
#  Chapter 1  ·  Mission 2 — "Walk the Square"
#  Load world:  chapter1_corridor.py
# ─────────────────────────────────────────────────────────────────
#
#  OBJECTIVE
#  Drive Robby in a square path — four equal sides, four 90° right turns.
#  Use a for loop so you only write the movement code ONCE.
#
#  NEW CONCEPT — for LOOP
#    for side in range(4):   ← repeats the indented block 4 times
#        drive(...)          ← these two lines run 4 times in a row
#        time.sleep(...)
#
#  range(4) produces the numbers  0, 1, 2, 3
#  On each repeat, 'side' holds the current number (0, 1, 2, 3).
#  (We don't use 'side' in the body here — we just need 4 repeats.)
#
#  WHAT TO OBSERVE
#  ───────────────
#  1. Does Robby return to exactly her starting position?
#     Probably not quite.  Why?  (Open-loop control — no sensor feedback.)
#
#  2. What happens if you change SIDE_TIME or TURN_TIME slightly?
#     Try  TURN_TIME = 0.28  and  TURN_TIME = 0.34  — observe the
#     difference in the corner angles.
#
#  3. What shape do you get if you change range(4) to range(3)?
#     What about range(6)?
#
#  CHALLENGE
#  Make Robby trace a rectangle instead of a square:
#    - long sides use SIDE_TIME = 2.0
#    - short sides use SIDE_TIME = 1.0
#  Hint: you'll need two different for loops, or an if statement
#        inside the loop.  Try both.
# ─────────────────────────────────────────────────────────────────

import time

# ── Tunable parameters ────────────────────────────────────────────
SPEED     = 0.4    # forward speed  (try 0.2 and 0.7 — same shape?)
SIDE_TIME = 1.5    # seconds per side  (≈ 2.2 m per side at SPEED=0.4)
TURN_TIME = 0.31   # seconds for a 90° right turn at angular=1.0

# ── Status report ─────────────────────────────────────────────────
print(f"Square path start.  Battery: {battery_level()}%")
print(f"Settings: speed={SPEED}, side={SIDE_TIME}s, turn={TURN_TIME}s")

# ── Drive the square ──────────────────────────────────────────────
for side in range(4):
    print(f"  Side {side + 1} of 4 ...")

    # Drive one side
    drive(SPEED, 0.0)
    time.sleep(SIDE_TIME)

    # Turn right 90°  (angular = +1.0 → clockwise)
    drive(0.0, 1.0)
    time.sleep(TURN_TIME)

# Always stop at the end
drive(0.0, 0.0)

print(f"Square complete.  Battery: {battery_level()}%")
print("Did Robby end up back where she started?")
