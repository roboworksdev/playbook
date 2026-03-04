# ─────────────────────────────────────────────────────────────────
#  Chapter 3  ·  Mission 1 — "Make Contact"
#  Load world:  chapter3_warehouse.py
# ─────────────────────────────────────────────────────────────────
#
#  OBJECTIVE
#  Navigate Robby to Crate_1 (the nearest orange crate, NE of start)
#  and magnetically attach to it.
#
#  NEW CONCEPTS
#  ────────────
#  close_enough()  →  returns True when a moveable object is within
#                     0.65 m of Robby's surface.  Use it to know when
#                     to stop approaching and attach.
#
#  attach()        →  couples Robby to the nearest object.
#                     Nothing happens if no object is close_enough().
#
#  holding()       →  returns True if Robby is currently carrying
#                     an attached object.
#
#  THE MISSION
#  ───────────
#  1. Run this script.  Watch Robby navigate to the orange crate
#     and attach.  The crate should lock onto Robby.
#
#  2. Read the console.  What does  holding()  return before and
#     after  attach() ?
#
#  3. Drive Robby manually (W/A/S/D keys) after the script ends.
#     Does the crate move with her?
#
#  KEY INSIGHT
#  while not close_enough(): drive(0.2, 0.0)
#  ──────────────────────────────────────────
#  Robby approaches slowly until the sensor says she's near enough.
#  This is closed-loop control — she adapts to the real distance,
#  not a fixed sleep time.  The approach always works, regardless
#  of exact timing.
#
#  CHALLENGE
#  Can you navigate Robby to Crate_2 (at x=7.0, y=4.0) instead?
#  Hint: change the navigation steps in Part 1.
# ─────────────────────────────────────────────────────────────────

import time

print(f"Mission 1 start.  Battery: {battery_level()}%")
print(f"Carrying anything? {holding()}")
print()
print("Navigating to Crate_1 at (3.5, 4.0) ...")
print()

# ── Part 1 — navigate east to x = 3.5 ────────────────────────────
print("Step 1: turning east ...")
drive(0.0, 1.0)       # turn right (face east)
time.sleep(0.30)
drive(0.0, 0.0)

print("Step 2: driving east 1.5 m ...")
drive(0.4, 0.0)       # drive east
time.sleep(0.52)      # ≈ 1.5 m at 2.88 m/s
drive(0.0, 0.0)

# ── Part 2 — turn north and approach until close enough ───────────
print("Step 3: turning north ...")
drive(0.0, -1.0)      # turn left (face north)
time.sleep(0.30)
drive(0.0, 0.0)

print("Step 4: approaching Crate_1 ...")
print(f"  Distance ahead: {distance(0):.2f} m")

while not close_enough():
    drive(0.2, 0.0)   # slow approach

drive(0.0, 0.0)
print(f"  close_enough() = {close_enough()}  — crate within reach!")
print()

# ── Part 3 — attach ───────────────────────────────────────────────
print("Attaching ...")
attach()

print()
print(f"holding()  = {holding()}")
print(f"Battery    = {battery_level()}%")
print()
if holding():
    print("Success! Crate_1 is attached.")
    print("Run Mission 2 to deliver it to the drop zone.")
else:
    print("No crate attached.  Is Robby close enough?")
    print(f"Gap ahead: {distance(0):.2f} m  (need distance-to-surface < 0.65 m)")
