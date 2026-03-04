# ─────────────────────────────────────────────────────────────────
#  Chapter 2  ·  Mission 2 — "Stop Before You Hit"
#  Load world:  chapter2_dark_room.py
# ─────────────────────────────────────────────────────────────────
#
#  OBJECTIVE
#  Make Robby drive north, but stop automatically before she
#  collides with Pillar_A.  The stopping distance is controlled
#  by a single variable — change it and see what happens.
#
#  NEW CONCEPT — while LOOP with a SENSOR CONDITION
#  ─────────────────────────────────────────────────
#    while distance(0) > STOP_GAP:
#        drive(0.4, 0.0)
#    drive(0.0, 0.0)
#
#  The loop keeps running while the condition is True.
#  Each iteration: Robby moves a little, the sensor is re-read,
#  the condition is checked again.
#  The moment distance(0) ≤ STOP_GAP, the loop exits.
#
#  THE MISSION
#  ───────────
#  1. Run this script.  Note exactly where Robby stops.
#     Read the final gap in the console.
#
#  2. Change  STOP_GAP = 0.8  to  STOP_GAP = 1.5  and run again.
#     Robby stops further back.  One variable — different behaviour.
#
#  3. Change  STOP_GAP = 0.3  and run again.
#     Robby stops very close.  Does she ever touch the pillar?
#
#  4. PREDICT before running:  if STOP_GAP = 5.0,  does Robby move?
#     Why or why not?
#
#  KEY INSIGHT
#  The loop is REACTIVE — it responds to the real world in real
#  time.  This is the difference between open-loop (drive for N
#  seconds, hope for the best) and closed-loop control (drive
#  until the sensor says stop).
#
#  COMMON MISCONCEPTION
#  if distance = 0.8     ← assignment:  sets distance to 0.8 (WRONG)
#  if distance(0) < 0.8  ← comparison:  checks if reading < 0.8  ✓
#  Robby's error message will appear if you write the first form.
#  This error is the lesson — read it carefully.
#
#  CHALLENGE
#  After stopping, print the distance readings in all 4 cardinal
#  directions.  Which direction has the most space?
#  Then add code to turn Robby to face that direction.
# ─────────────────────────────────────────────────────────────────

import time

# ── Change this one value — the whole behaviour adapts ────────────
STOP_GAP = 0.8    # ← try 1.5, 0.5, 0.3

# ─────────────────────────────────────────────────────────────────
print(f"Mission 2 start.  Battery: {battery_level()}%")
print(f"Stop gap: {STOP_GAP} m  |  Obstacle ahead: {distance(0):.2f} m")
print()

# Check: is there already an obstacle within STOP_GAP?
if distance(0) <= STOP_GAP:
    print("Obstacle already within stop gap — not moving.")
    print("Increase STOP_GAP or clear the path.")
else:
    print("Driving north ...")
    while distance(0) > STOP_GAP:
        drive(0.4, 0.0)
    drive(0.0, 0.0)
    print()
    print(f"Stopped.  Gap ahead: {distance(0):.2f} m  (target: {STOP_GAP} m)")
    print(f"Battery after drive: {battery_level()}%")
    print()
    print("Surroundings at stop point:")
    print(f"  Ahead  (  0°): {distance(0):.2f} m")
    print(f"  Right  ( 90°): {distance(90):.2f} m")
    print(f"  Behind (180°): {distance(180):.2f} m")
    print(f"  Left   (270°): {distance(270):.2f} m")
